from teampages.models import Team, Player

from teampages.ODSUtil.ODSReader import ODSReader

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
		import pdb; pdb.set_trace()
		if clear:
			Player.objects.filter(owner=self.team).update(active=False, owner=None)
		for player in self.roster:
			player.owner=self.team
			if player in self.lineup:
				player.active=True
			player.save()
