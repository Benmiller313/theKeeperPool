from django.conf.urls import patterns, include, url

urlpatterns = patterns('teampages.views', 
	url(r'teams/(?P<team_name>\w+)/$', 'teampage'),
	url(r'players/(?P<player_id>\d+)/$', 'playerpage'),
	url(r'transactions/$', 'transactions'),
	url(r'drafts/$', 'drafts'),
)