from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone

from teampages.models import Team, Banner, FAPickup
import math
from datetime import datetime, MINYEAR

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
	picks_template = "teampages/teams/picks/"+team_name+".html"

	context = {	
		"team": team,
		"teams": teams,
		"banners": sorted(banners.iteritems(), reverse=True),
		"roster_template": roster_template,
		"lineup_template": lineup_template,
		"picks_template": picks_template,
	}
	return render_to_response("teampages/teampage.html", context)

def rules(request):
	teams = list(Team.objects.all().order_by('name'))
	context = {"teams":teams}
	return render_to_response("teampages/rules.html", context)

def waiverOrder(request):
	teams = list(Team.objects.all().order_by('name'))

	#calculate the waiver order		

	waiver_order = [];
	for team in Team.objects.all().order_by('name'):
		pickups = FAPickup.objects.filter(team=team).order_by('date')
		if not pickups:
			waiver_order.append((team, None))
		else:
			waiver_order.append((team, pickups.latest('date')))

	def waiver_key(waiver):
		(team, pickup) = waiver
		if not pickup:
			if team.name=="Nick":
				return timezone.make_aware(datetime(year=2001, month=1, day=1), timezone.get_default_timezone())
			return timezone.make_aware(datetime(year=2000, month=1, day=1), timezone.get_default_timezone())
		else:
			return pickup.date

	waiver_order.sort(key=waiver_key)

	print waiver_order

	context = { 
		"teams": teams,
		"waiver_order": waiver_order,
	}
	return render_to_response("teampages/waiver_order.html", context)



