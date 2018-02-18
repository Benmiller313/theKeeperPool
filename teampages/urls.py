from django.conf.urls import patterns, include, url

urlpatterns = patterns('teampages.views', 
    url(r'teams/(?P<team_name>\w+)/$', 'teampage'),
    url(r'teamsv2/(?P<team_name>\w+)/$', 'teampage_v2'),
    url(r'players/(?P<player_id>\d+)/$', 'playerpage'),
    url(r'transactions/$', 'transactions'),
    url(r'drafts/$', 'drafts'),
    url(r'playerlist/$', 'playerlist')
)