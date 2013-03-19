from django.shortcuts import render_to_response, get_object_or_404

from .models import Country, CIAWFBEntry, CIAWFBFieldInfo
from .ciawfbgroupedfieldlist import get_CIAWFB_grouped_fields, get_CIAWFB_group_list


def index(request):
    country_list = Country.objects.all().order_by('CIAWFB_name_short')
    return render_to_response('index.html', {'country_list': country_list})


def country(request, url_name):
    def return_field_set(group_name, entry, field_info):
        field_set = []
        for field_db_name in get_CIAWFB_grouped_fields()[group_name]:
            field_value = getattr(CIAWFB_entry, field_db_name)
            field_info_object = CIAWFBFieldInfo.objects.filter(field_dbname=field_db_name)[0]
            field_desc = field_info_object.field_description
            field_title = field_info_object.field_name
            field_set.append((field_title, field_desc, field_value, field_db_name))
        return field_set

    country = get_object_or_404(Country, url_name=url_name)
    CIAWFB_entry = CIAWFBEntry.objects.filter(country__id=country.id).order_by('-date_entered')[0]
    CIAWFB_field_info = CIAWFBFieldInfo.objects.all()

    all_field_sets = []
    for group_title in get_CIAWFB_group_list():
        all_field_sets.append((group_title, return_field_set(group_title, CIAWFB_entry, CIAWFB_field_info)))

    return render_to_response('countrydetail.html',
                              {'country': country,
                               'date_entered': CIAWFB_entry.date_entered,
                               'all_field_sets': all_field_sets
                               }
                              )
