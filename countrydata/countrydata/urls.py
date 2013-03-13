from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'main.views.index'),
                       url(r'^country/(?P<country_short_name>.*)/$', 'main.views.country'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
