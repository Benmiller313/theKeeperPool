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

class FAPickup(models.Model):
	team = models.ForeignKey(Team)
	player = models.CharField(max_length=256)
	injured = models.BooleanField()
	date = models.DateTimeField()

	def __unicode__(self):
		return self.team.name + " - " + self.player


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

	def full_name(self):
		return self.last_name + ', ' + self.first_name