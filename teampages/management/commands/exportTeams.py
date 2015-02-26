
from django.core.management.base import BaseCommand, CommandError

from teampages.models import Team, DraftPick, Player

from teampages.TeamManagement.SpreadsheetDB import SheetWriter

class Command(BaseCommand):
    help = 'export teams to the spreatsheet'

    def handle(self, *args, **options):
    	if len(args) > 0:
    		for team_name in args:
    			self.writeSheet(Team.objects.get(name=team_name))
    	else:
    		for team in Team.objects.all():
    			self.writeSheet(team)

    def writeSheet(self, team):
    	print "exporting " + team.name
    	db = SheetWriter("test_keeperpool20142015.ods")
    	db.writeTeam(team)
        db.db.close()

