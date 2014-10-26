from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from teampages.models import Team, Banner
import math

def home(request):
	teams = list(Team.objects.all().order_by("name"))
	context = {"teams":teams}
	return render_to_response("teampages/home.html", context)


def teampage(request, team_name):
	team = get_object_or_404(Team, name=team_name)
	teams = list(Team.objects.all().order_by("name"))

	#banners by year
	banners = {}
	years = Banner.objects.filter(team__name=team_name).order_by('-year').values('year').distinct()
	for val in years:
		banners[val["year"]] = list(Banner.objects.filter(team__name=team_name, year=val["year"]))
	roster_template = "teampages/teams/rosters/"+team_name+".html"
	lineup_template = "teampages/teams/lineups/"+team_name+".html"

	context = {	
		"team": team,
		"teams": teams,
		"banners": sorted(banners.iteritems(), reverse=True),
		"roster_template": roster_template,
		"lineup_template": lineup_template,
	}
	return render_to_response("teampages/teampage.html", context)

def rules(request):
	teams = list(Team.objects.all().order_by('name'))
	context = {"teams":teams}
	return render_to_response("teampages/rules.html", context)