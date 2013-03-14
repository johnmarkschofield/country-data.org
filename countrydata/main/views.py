from django.shortcuts import render_to_response, get_object_or_404

from .models import Country, CIAWFBEntry


def index(request):
    country_list = Country.objects.all().order_by('CIAWFB_name_short')
    return render_to_response('index.html', {'country_list': country_list})


def country(request, url_name):
    country = get_object_or_404(Country, url_name=url_name)
    latestentry = CIAWFBEntry.objects.filter(country__id=country.id).order_by('-date_entered')[0]
    return render_to_response('countrydetail.html',
                              {'country': country,
                               'CIAWFB_entry': latestentry})
