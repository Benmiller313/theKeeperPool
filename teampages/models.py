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