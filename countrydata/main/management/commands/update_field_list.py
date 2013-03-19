# Standard Library Imports
import urllib2
import re

# Core Django Imports
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_str

# Third Party App Imports
import bs4

# This App Imports
from main.models import CIAWFBFieldInfo, CIAWFBEntry
import main.ciawfbgroupedfieldlist
from updatecountries import field_data_codes


class Command(BaseCommand):
    help = 'Checks field data for errors, and outputs any missing fields.'

    def handle(self, *args, **options):

        def extract_field_data():
            """ Note: Requires HTML5 Library: pip intall html5lib
            """

            fullURL = "https://www.cia.gov/library/publications/the-world-factbook/docs/notesanddefs.html"
            soup = bs4.BeautifulSoup(urllib2.urlopen(fullURL).read())
            field_data = []

            tables = soup.find_all('table', width="638", id=re.compile('^\d\d\d\d$'))
            for table in tables:
                try:
                    title = table.find('td', class_="category_titles").text.strip()
                except AttributeError:
                    continue

                try:
                    field_desc = table.find('div', class_="category_data").text.encode('utf-8').strip()
                except AttributeError:
                    continue

                try:
                    field_list_url = table.find('a', href=re.compile(r'^../fields/\d\d\d\d.html'))['href']
                except (AttributeError, TypeError):
                    continue
                field_data.append((title, field_desc, field_list_url))
            return field_data

        field_data = extract_field_data()

        # Set up a sample CIAWFB Entry to test against
        sample_CIAWFB_model = CIAWFBEntry.objects.filter(country__id=1)
        model_field_names = sample_CIAWFB_model[0]._meta.get_all_field_names()
        live_site_field_names = []

        group_list = main.ciawfbgroupedfieldlist.get_CIAWFB_group_list()
        grouped_fields = main.ciawfbgroupedfieldlist.get_CIAWFB_grouped_fields()

        for field_trio in field_data:
            title = smart_str(field_trio[0].strip()).decode('ascii', 'ignore')
            db_title = slugify(title).replace('-', '_').rstrip('_')
            live_site_field_names.append(db_title)
            desc = field_trio[1].strip().decode('ascii', 'ignore')

            # Verify that fields from live CIAWFB are in model
            if db_title not in model_field_names:
                print('ERROR: Field name "%s" is in the live CIAWFB site but not in models.py.' % db_title)

            # Verify that fields from live CIAWFB are in groupedfieldlist:
            field_matches = False
            for group in group_list:
                if db_title in grouped_fields[group]:
                    field_matches = True
                    break
            if field_matches is False:
                print('ERROR: Field name "%s" is in the live CIAWFB site but is not in the grouped field list.'
                      % db_title)

            # Verify that fields from live CIAWFB are in updatecountries.field_data_codes
            if db_title not in field_data_codes.keys():
                print('ERROR: Field name "%s" is in the live CIAWFB site but is not in updatecountries field_data_codes' %
                      db_title)

            # Write field name, field description to database.
            try:
                CIAWFB_order_entry = CIAWFBFieldInfo.objects.get(field_dbname=db_title)
            except CIAWFBFieldInfo.DoesNotExist:
                CIAWFB_order_entry = CIAWFBFieldInfo(field_dbname=db_title)
            CIAWFB_order_entry.field_description = desc
            CIAWFB_order_entry.field_name = title
            CIAWFB_order_entry.save()

        # Verify that fields from model are in live CIAWFB
        for field_name in model_field_names:
            if field_name not in live_site_field_names:
                if field_name not in ['country', 'date_entered', 'id']:
                    print('ERROR: Field name "%s" is in models.py but is not in the live CIAWFB site.' %
                          field_name)

        # Verify that fields from grouped field list are in live CIAWFB
        for group in group_list:
            for field_name in grouped_fields[group]:
                if field_name not in live_site_field_names:
                    print('ERROR: Field name "%s" is in live CIAWFB site but is not in the grouped field list.' %
                          field_name)

        # Verify that fields from field_data_codes are in live CIAWFB
        for field_name in field_data_codes.keys():
            if field_name not in live_site_field_names:
                print('ERROR: Field name "%s" is in live CIAWFB site but is not in the field_data_codes.' %
                      field_name)
