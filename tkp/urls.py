from django.conf.urls import patterns, include, url
from ajax_select import urls as ajax_select_urls
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tkp.views.home', name='home'),
    # url(r'^tkp/', include('tkp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include("teampages.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookup/', include(ajax_select_urls)),
    url(r'^lookup/', include(ajax_select_urls)),
    url(r'^$', 'teampages.views.home', name='home'),
	url(r'^rules/$', 'teampages.views.rules', name="rules"),
    url(r'^waiverorder/$', 'teampages.views.waiverOrder', name='waiverOrder'),
)
