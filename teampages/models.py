from django.db import models


class Team(models.Model):
	name = models.CharField(max_length=256)
	mascot_image = models.CharField(max_length=256)

	def __unicode__(self):
		return self.name

class Trophy(models.Model):
	name = models.CharField(max_length=256)
	
	def __unicode__(self):
		return self.name

class Banner(models.Model):
	trophy = models.ForeignKey(Trophy)
	team = models.ForeignKey(Team)
	year = models.IntegerField()
	player = models.CharField(max_length=256, blank=True, default="")

	def __unicode__(self):
		return self.trophy.name + " - " + str(self.year)


class Player(models.Model):
	id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	position = models.CharField(max_length=2)
	salary = models.IntegerField()
	nhl_team = models.CharField(max_length=4)
	owner = models.ForeignKey(Team, null=True, blank=True, default = None)
	active = models.BooleanField(default=False)
	in_waivers = models.BooleanField(default=False)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name + '\n' + self.nhl_team + '\n' + self.position + '\n' + unicode(self.salary) + '\n'

	def fullName(self):
		return self.last_name + ', ' + self.first_name


class DraftPick(models.Model):
	year = models.IntegerField()
	round = models.IntegerField()
	owner = models.ForeignKey(Team, related_name="current_picks")
	original_owner = models.ForeignKey(Team, related_name="original_picks")
	player = models.ForeignKey(Player, null=True)

	def __unicode__(self):
		return self.original_owner.name + "'s " + str(self.year) + " round " + str(self.round) 

class FAPickup(models.Model):
	team = models.ForeignKey(Team)
	player = models.CharField(max_length=256)
	player_added = models.ForeignKey(Player,related_name="player_added")
	player_dropped = models.ForeignKey(Player, related_name="player_dropped")
	injured = models.BooleanField()
	date = models.DateTimeField()

	def __unicode__(self):
		return self.team.name + " - " + self.player


class Trade(models.Model):
	teamA = models.ForeignKey(Team, related_name="teamA")
	teamB = models.ForeignKey(Team, related_name="teamB")
	players_received_a = models.ManyToManyField(Player, related_name="players_received_a")
	players_received_b = models.ManyToManyField(Player, related_name="players_received_b")
	picks_received_a = models.ManyToManyField(DraftPick, related_name="picks_received_a")
	picks_received_b = models.ManyToManyField(DraftPick, related_name="picks_received_b")
	date = models.DateTimeField()


