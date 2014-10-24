from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from teampages.models import Team
import math

def home(request):
	teams = list(Team.objects.all().order_by("name"))
	context = {"teams":teams}
	return render_to_response("teampages/home.html", context)


def teampage(request, team_name):
	team = get_object_or_404(Team, name=team_name)
	teams = list(Team.objects.all().order_by("name"))
	roster_template = "teampages/teams/rosters/"+team_name+".html"
	lineup_template = "teampages/teams/lineups/"+team_name+".html"

	context = {	
		"team": team,
		"teams": teams,
		"roster_template": roster_template,
		"lineup_template": lineup_template,
	}
	return render_to_response("teampages/teampage.html", context)

def rules(request):

	return render_to_response("teampages/rules.html")