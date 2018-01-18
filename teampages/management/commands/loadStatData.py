from django.core.management.base import BaseCommand, CommandError

from teampages.statScrapper import load_all_stats

class Command(BaseCommand):
	help = 'Reloads Stat Database'

	def handle(self, *args, **options):
		load_all_stats()
		print "done!"