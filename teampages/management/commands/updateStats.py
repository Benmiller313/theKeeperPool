from django.core.management.base import BaseCommand, CommandError

from teampages.statScrapper import load_new_stats

class Command(BaseCommand):
	help = 'Reloads Stat Database'

	def handle(self, *args, **options):
		load_new_stats()
		print "done!"