from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.utils import timezone
from django import forms
from django.db.models import Q, Sum
from ajax_select.fields import AutoCompleteSelectField
import django_tables2 as tables

from teampages.models import Team, Banner, FAPickup, Player, Trade, DraftPick, Draft, Stat
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


def teampage_v2(request, team_name):

    return render_to_response("teampages/teampage.html", context)



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


    drafts = Draft.objects.filter(finished=False)
    picks = {draft.year : DraftPick.objects.filter(owner=team, draft=draft) for draft in drafts}

    context = {
        "team": team,
        "teams": teams,
        "banners": sorted(banners.iteritems(), reverse=True),
        "roster": {
            "players": {
                "F": Player.objects.filter(owner=team, position="F"),
                "D": Player.objects.filter(owner=team, position="D"),
                "G": Player.objects.filter(owner=team, position="G"),
            },
            "salary": Player.objects.filter(owner=team).aggregate(Sum('salary'))["salary__sum"]

        },
        "lineup": {
            "players" : {
                "F": Player.objects.filter(owner=team, position="F", active=True),
                "D": Player.objects.filter(owner=team, position="D", active=True),
                "G": Player.objects.filter(owner=team, position="G", active=True),
            },
            "salary": Player.objects.filter(owner=team, active=True).aggregate(Sum('salary'))["salary__sum"]
        },
        "picks": picks,
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

def _formatTransactions(trades, pickups, draftpicks):
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
            "left_aq": [pickup.player_added.fullName()] if pickup.player_added else None,
            "right_aq": [pickup.player_dropped.fullName()] if pickup.player_dropped else None,
            })

    if draftpicks:
        draftpicks = [{"type":"Drafted", "date": pick.draft.date, "pick":pick} for pick in draftpicks]
    else:
        draftpicks = []

    transaction_list = sorted(formatted_pickups + formatted_trades + draftpicks, key=lambda trans: trans["date"], reverse=True)
    return transaction_list


def playerpage(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    teams = list(Team.objects.all().order_by('name'))
    trades = list(Trade.objects.filter(players_received_a=player)) +  list(Trade.objects.filter(players_received_b=player))
    pickups = FAPickup.objects.filter(Q(player_added=player) | Q(player_dropped=player))
    draftpicks = DraftPick.objects.filter(player=player)

    transaction_list = _formatTransactions(trades, pickups, draftpicks)

    stats = Stat.objects.filter(player=player).order_by("-year")
    context={
        "teams": teams,
        "player":player,
        "transaction_list":transaction_list,
        "stats":stats,
    }

    return render_to_response("teampages/playerpage.html", context)


def transactions(request):
    teams = list(Team.objects.all().order_by('name'))

    trades = Trade.objects.all().order_by('-date')
    pickups = FAPickup.objects.all().order_by('-date')



    transaction_list = _formatTransactions(trades, pickups, None)

    context = {
        "transaction_list": transaction_list,
        "teams":teams,
    }

    return render_to_response("teampages/transactions.html", context)

def drafts(request):
    teams = list(Team.objects.all().order_by('name'))

    drafts = Draft.objects.filter(finished=True).order_by("-date")

    context = {
        "teams":teams,
        "drafts": drafts,
    }

    return render_to_response("teampages/drafts.html", context)


class playerTable(tables.Table):
    class Meta:
        model = Player
        exclude = ("id", "in_waivers")
        attrs = {"class": "paleblue"}

def _filterPlayers(request):
    players = Player.objects.all()
    if request.GET.get("filter_position"):
        players = players.filter(position=request.GET.get("filter_position"))
    if request.GET.get("filter_owned"):
        if request.GET.get("filter_owned") == "FA":
            players = players.filter(owner=None)
        elif request.GET.get("filter_owned") == "Owned":
            players = players.exclude(owner=None)
    return players


def playerlist(request):
    teams = list(Team.objects.all().order_by('name'))
    table = playerTable(_filterPlayers(request))
    tables.RequestConfig(request).configure(table)
    context = {
        "teams":teams,
        "table" : table

    }

    return render(request, "teampages/playerlist.html", context)










