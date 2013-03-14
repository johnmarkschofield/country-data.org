from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'main.views.index'),
                       url(r'^country/(?P<url_name>.*)/$', 'main.views.country'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
