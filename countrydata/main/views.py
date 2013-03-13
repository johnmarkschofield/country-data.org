from django.shortcuts import render_to_response, get_object_or_404

from .models import Country, CIAWFBEntry


def index(request):
    country_list = Country.objects.all()
    return render_to_response('index.html', {'country_list': country_list})


def country(request, country_short_name):
    country = get_object_or_404(Country, CIAWFB_name_short=country_short_name)
    country_id = country.id
    latestentry = CIAWFBEntry.objects.filter(country__id=country_id).order_by('-date_entered')[0]
    return render_to_response('countrydetail.html',
                              {'country': country,
                               'CIAWFB_latest_entry': latestentry})
