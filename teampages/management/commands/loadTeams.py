
from django.core.management.base import BaseCommand, CommandError

from teampages.models import Team, DraftPick, Player

from teampages.TeamManagement.SpreadsheetDB import SheetReader

class Command(BaseCommand):
    help = 'load the teams'

    def handle(self, *args, **options):
        if len(args) > 0:
            for team_name in args:
                Player.objects.filter().update(active=False, owner=None)
                self.loadSheet(Team.objects.get(name=team_name))
        else:
            Player.objects.filter().update(active=False, owner=None)
            for team in Team.objects.all():
                self.loadSheet(team)

    def loadSheet(self, team):
        print "loading " + team.name
        db = SheetReader(team)
        db.importTeamData(clear=True)

