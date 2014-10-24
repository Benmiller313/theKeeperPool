from django.conf.urls import patterns, include, url

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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'teampages.views.home', name='home'),
    url(r'^teams/', include("teampages.urls")),
	url(r'^rules/$', 'teampages.views.rules', name="rules"),

)
