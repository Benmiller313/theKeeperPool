from django.core.management.base import BaseCommand, CommandError

from teampages.models import Team, DraftPick

class Command(BaseCommand):
    help = 'Generate draftpicks for a given year'

    def handle(self, *args, **options):
    	if len(args) < 1:
    		print "Must enter a year"
    		return
    	try:
    		year = int(args[0])
    	except:
    		print"Must enter a year"
    		return

    	teams = Team.objects.all()
    	rounds = 6

    	for team in teams:
    		for round in range(1, rounds+1):
    			DraftPick(year=year, round=round, owner=team, original_owner=team).save()

