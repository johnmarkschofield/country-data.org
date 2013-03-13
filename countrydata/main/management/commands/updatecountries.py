import urllib2
import re

import bs4

from django.core.management.base import BaseCommand

from .models import Country, CIAWFBEntry

field_data_codes = {'agriculture_products': "2052"}

#https://www.cia.gov/library/publications/the-world-factbook/fields/2052.html


class Command(BaseCommand):
    help = 'Updates Country Data from CIA World Factbook'

    def handle(self, *args, **options):

        def extract_field_data(field_name, field_url):
            """ Note: Requires HTML5 Library: pip intall html5lib
            """
            country_attribute_list = {}

            rootURL = "https://www.cia.gov/library/publications/the-world-factbook/fields/"
            fullURL = rootURL + field_url + '.html'
            soup = bs4.BeautifulSoup(urllib2.urlopen(fullURL).read())
            tables = soup.find_all('table', width="638")
            for table in tables:
                try:
                    country = table.find('a', href=re.compile('geos')).text.strip()
                except AttributeError:
                    continue

                try:
                    field_value = table.find('td', class_="category_data").text.strip()
                except AttributeError:
                    continue
                country_attribute_list[country] = field_value
            return country_attribute_list

        for field_name in field_data_codes.keys():
            field_data = extract_field_data(field_name, field_data_codes[field_name])
            # next: https://docs.djangoproject.com/en/dev/intro/tutorial01/

