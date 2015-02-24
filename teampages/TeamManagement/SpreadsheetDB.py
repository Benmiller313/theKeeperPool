from teampages.models import Team, Player

from teampages.ODSUtil.ODSReader import ODSReader
from pyexcel_ods import ODSWriter

class SheetReader():

	def __init__(self, team):
			db = ODSReader("keeperpool20142015.ods")
			sheet =  db.getSheet(team.name + "'s Team")
			self.roster = []
			self.lineup = []
			self.picks = {}
			self.team = team

			for row in sheet: 
				print row
				try:
					self.roster.append(Player.objects.get(pk=row[0]))
				except:
					pass
				try:
					self.lineup.append(Player.objects.get(pk=row[4]))
				except:
					pass
				try:
					self.picks.setdefault(row[8], []).append(row[9])
				except:
					pass

	def importTeamData(self, clear=True):
		if clear:
			Player.objects.filter(owner=self.team).update(active=False, owner=None)
		for player in self.roster:
			player.owner=self.team
			if player in self.lineup:
				player.active=True
			player.save()


class SheetWriter():
	def __init__(self, filename):
		self.db = ODSWriter(filename)
		

	def _writePlayer(player):
		return [player.id, player.position, player.first_name, player.last_name, player.salary]
	def _writeDraftpick(pick):
		if pick.round == 1:
			round = "1st"
		elif pick.round ==2:
			round= "2nd"
		elif pick.round ==3:
			round= "3rd"
		else round = str(pick.round) + "th"
		return [pick.year, pick.original_owner.name + "'s " + round]

	def writeTeam(team):
		count_roster = len(team.player_set.all())
		count_lineup = len(team.player_set.filter(active=True))
		count_picks = len(team.current_picks.all())

		roster= list(team.player_set.all())
		lineup = list(team.player_set.filter(active=True))
		picks = list(team.current_picks.all())

		i = 0
		data = []
		while (i < count_roster or i < count_lineup or i < count_picks):
			data.append([])
			if i < count_roster:
				data[i] += _writePlayer(roster[i])



