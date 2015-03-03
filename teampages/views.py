from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django import forms
from django.db.models import Q
from ajax_select.fields import AutoCompleteSelectField

from teampages.models import Team, Banner, FAPickup, Player, Trade, DraftPick
import math
from datetime import datetime, MINYEAR


class PlayerSearchForm(forms.Form):
	q = AutoCompleteSelectField(
		'player',
		required=True,
		help_text="help_text",
		label="label",
		)



def home(request):

	teams = list(Team.objects.all().order_by("name"))
	context = {"teams":teams}
	initial = {'q': "\"This is an initial value,\" said O'Leary."}
	form=PlayerSearchForm()
	context["form"] = form
	if 'q' in request.GET:
		context['entered'] = request.GET.get('q')
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
		"roster": {
			"F": Player.objects.filter(owner=team, position="F"),
			"D": Player.objects.filter(owner=team, position="D"),
			"G": Player.objects.filter(owner=team, position="G"),
		},
		"lineup": {
			"F": Player.objects.filter(owner=team, position="F", active=True),
			"D": Player.objects.filter(owner=team, position="D", active=True),
			"G": Player.objects.filter(owner=team, position="G", active=True),
		},
		"picks": {year:DraftPick.objects.filter(owner=team, year=year) for year in 
			[pick["year"] for pick in DraftPick.objects.all().values('year').distinct()]},
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

def _formatTransactions(trades, pickups):
	formatted_trades = []
	for trade in trades:
		formatted_trades.append({
			"type": "Trade",
			"date": trade.date,
			"left_team": trade.teamA,
			"right_team": trade.teamB,
			"left_aq": [player.fullName() for player in trade.players_received_a.all()] + [str(pick) for pick in trade.picks_received_a.all()],
			"right_aq": [player.fullName() for player in trade.players_received_b.all()] + [str(pick) for pick in trade.picks_received_b.all()],
 			})

	formatted_pickups = []
	for pickup in pickups:
		formatted_pickups.append({
			"type": "FA Pickup",
			"date": pickup.date,
			"left_team": pickup.team, 
			"right_team": pickup.team,
			"left_aq": [pickup.player_added.fullName()],
			"right_aq": [pickup.player_dropped.fullName()],
			})


	transaction_list = sorted(formatted_pickups + formatted_trades, key=lambda trans: trans["date"], reverse=True)
	return transaction_list


def playerpage(request, player_id):
	player = get_object_or_404(Player, id=player_id)
	teams = list(Team.objects.all().order_by('name'))

	trades = Trade.objects.filter(Q(players_received_a=player) | Q(players_received_b=player))
	pickups = FAPickup.objects.filter(Q(player_added=player) | Q(player_dropped=player))

	transaction_list = _formatTransactions(trades, pickups)


	context={
		"teams": teams, 
		"player":player,
		"transaction_list":transaction_list,
	}

	return render_to_response("teampages/playerpage.html", context)


def transactions(request):
	teams = list(Team.objects.all().order_by('name'))

	trades = Trade.objects.all().order_by('-date')
	pickups = FAPickup.objects.all().order_by('-date')


	transaction_list = _formatTransactions(trades, pickups)

	context = {
		"transaction_list": transaction_list,
		"teams":teams,
	}

	return render_to_response("teampages/transactions.html", context)





