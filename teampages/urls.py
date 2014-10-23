from django.conf.urls import patterns, include, url

urlpatterns = patterns('teampages.views', 
	url(r'^(?P<team_name>\w+)/$', 'teampage'),
)