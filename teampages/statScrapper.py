from bs4 import BeautifulSoup
from urllib2 import urlopen

from teampages.models import Player, Stat

PLAYER_URL="http://stats.nhlnumbers.com/player_stats/{}"


col_ordering = ""

def get_stat_rows(soup):
	return soup.find(id='stats-data').find('tbody').find_all("tr")





def load_all_stats():
	Stat.objects.all().delete()
	for player in Player.objects.all():
		print "Loading " + player.fullName()
		url = PLAYER_URL.format(player.id)
		html = urlopen(url).read()
		soup = BeautifulSoup(html, "html.parser")
		stat_rows = get_stat_rows(soup)
		for row in stat_rows:
			cols = [col.string for col in row.find_all("td")]
			if player.position != "G":
				Stat(
					player=player,
					year=cols[0],
					season=cols[1],
					games_played=int(cols[2]),
					goals=int(cols[3]),
					assists=int(cols[4]),
					points=int(cols[5]),
					plus_minus=int(cols[6]),
					short_handed_goals=int(cols[12]),
					game_winning_goals=int(cols[14]),
				).save()
			else:
				Stat(
					player=player,
					year=int(cols[0]),
					season=cols[1],
					games_played=int(cols[2]),
					wins=int(cols[5]),
					shutouts=int(cols[14])
				).save()
