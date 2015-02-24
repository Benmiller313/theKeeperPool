from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import os
from django.core.management.base import BaseCommand, CommandError
from teampages.models import Player

BASE_URL = "http://nhlnumbers.com/"


def get_team_links(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "html.parser")
	links = [dd['href'] for dd in soup.find_all('a', 'team')]
	return links

def get_player_rows(team_url):
	html=urlopen(team_url).read()
	soup = BeautifulSoup(html, "html.parser")
	return soup.find_all('tr')		

def get_all_players():
	for link in get_team_links(BASE_URL):
		team = get_team_from_url(link)
		trs = get_player_rows(link)
		for row in trs:
			nameCell = row.find('td', 'team-cell')
			if nameCell and row.td.a.has_key('title') and check_if_real_player(row):	#if this is a player row
				player = Player()

				id_match = re.match(r'/player_stats/(\d+)-', row.td.a['href'])
				player.id = id_match.group(1)
				name = nameCell.a.string.split(',')
				player.first_name = name[1].strip()
				player.last_name = name[0].strip()
				player.position = parse_player_link_title(row.td.a['title'], name)[0]
				player.salary = get_player_salary(row)
				player.nhl_team = team
				#print player
				player.save()
def get_team_from_url(url):
	#print url
	team = re.search('/teams/(.*)', url).group(1)
	return team

def parse_player_link_title(title, name):
	position = re.search('Position: (.*)<br />', title).group(1)
	if position == 'Center' or position == 'Left' or position == 'Right':
		position = 'Forward'

	check =re.search('Retained Salary (.*)<', title)
	if check:
		print name[0], name[1], check.group(1)

	return position

def check_if_real_player(row):
	if row.find('a', 'buyout'):
		return False
	else:
		return True

def get_player_salary(player_row):
	raw_salary = float(player_row.find('td', 'capnumber').string)
	return int(raw_salary* 1000000)


class Command(BaseCommand):
	help = 'Reload the player database'

	def handle(self, *args, **options):
		Player.objects.all().delete()
		get_all_players()
