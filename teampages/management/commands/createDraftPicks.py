from django.core.management.base import BaseCommand, CommandError

from teampages.models import Team, DraftPick, Draft

class Command(BaseCommand):
	help = 'Generate draftpicks for a given year'

	def handle(self, *args, **options):
		if len(args) < 2:
			print "Must enter a year and name"
			return
		try:
			year = int(args[0])
		except:
			print"Must enter a year"
			return
		draft = Draft(year=year, name=args[1])
		draft.save()
		teams = Team.objects.all()
		rounds = 7
		for team in teams:
			for round in range(1, rounds+1):
				if not DraftPick.objects.filter(draft__year=year, round=round, original_owner=team).exists():
					DraftPick(draft=draft, round=round, owner=team, original_owner=team).save()

