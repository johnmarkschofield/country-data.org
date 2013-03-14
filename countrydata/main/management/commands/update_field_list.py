import urllib2
import re

import bs4

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_str


class Command(BaseCommand):
    help = 'Outputs field list data to be put in updatecountries.py, countrydetail.html, and models.py. Output must be hand-edited into those files.'

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

        updatecountries_fo = open('updatecountries_new.py', 'wt')
        models_fo = open('models_new.py', 'wt')
        template_fo = open('template_new.py', 'wt')

        for field_trio in field_data:
            title = smart_str(field_trio[0].strip()).decode('ascii', 'ignore')
            db_title = slugify(title).replace('-', '_')
            desc = field_trio[1].strip().decode('ascii', 'ignore')
            url_code = re.search(r'fields/(\d\d\d\d).html', field_trio[2]).expand(r'\1').decode('ascii', 'ignore')

            updatecountries_fo.write(u"'%s': '%s',\n" % (db_title, url_code))
            models_fo.write(u"%s = models.CharField(max_length=200, blank=True, null=True)\n" % db_title)
            template_string = u'<h4 class="field_name">%s</h4>\n<p class="field_definition">%s</p>\n<p class="field_content">{{ CIAWFB_entry.%s }}</p>\n\n' % (title, desc, db_title)
            template_fo.write(template_string.decode('ascii', 'ignore'))
        updatecountries_fo.close()
        models_fo.close()
        template_fo.close()
