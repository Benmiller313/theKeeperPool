
from django.core.management.base import BaseCommand, CommandError

from teampages.models import Team, DraftPick, Player

from teampages.TeamManagement.SpreadsheetDB import SheetReader

class Command(BaseCommand):
    help = 'Load a the team spreadsheets into the database'

    def handle(self, *args, **options):
    	if len(args) > 0:
    		for team_name in args:
    			self.loadSheet(Team.objects.get(name=team_name))
    	else:
    		for team in Team.objects.all():
    			self.loadSheet(team)

    def loadSheet(self, team):
    	print "loading " + team.name
    	db = SheetReader(team)
    	db.importTeamData()

