from django.db import models


class Team(models.Model):
	name = models.CharField(max_length=256)
	mascot_image = models.CharField(max_length=256)

	def __unicode__(self):
		return self.name

	def totalSalary(self):
		all_sal = [player.salary for player in self.player_set.all()]
		return sum(all_sal)

	def lineupSalary(self):
		roster_sal = [player.salary for player in self.player_set.filter(active=True)]
		return sum(roster_sal)


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
	first_name = models.CharField(max_length=100, verbose_name="First name")
	last_name = models.CharField(max_length=100, verbose_name="Last name")
	position = models.CharField(max_length=2, verbose_name="Position")
	salary = models.IntegerField(verbose_name="Salary")
	nhl_team = models.CharField(max_length=4, verbose_name="NHL team")
	owner = models.ForeignKey(Team, null=True, blank=True, default = None, verbose_name="Owner")
	active = models.BooleanField(default=False, verbose_name="Active")
	in_waivers = models.BooleanField(default=False, verbose_name="In waivers")

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name + '\n' + self.nhl_team + '\n' + self.position + '\n' + unicode(self.salary) + '\n'

	def fullName(self):
		return self.last_name + ', ' + self.first_name

class Draft(models.Model):
	name = models.CharField(max_length=256)
	year = models.IntegerField()
	teams = models.ManyToManyField(Team, through='DraftOrder')
	date = models.DateTimeField(null=True, blank=True)
	finished = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name


class DraftOrder(models.Model):
	team = models.ForeignKey(Team)
	draft = models.ForeignKey(Draft)
	order = models.IntegerField()


class DraftPick(models.Model):
	draft = models.ForeignKey(Draft)
	pick_number = models.IntegerField(null=True, blank=True)
	round = models.IntegerField()
	owner = models.ForeignKey(Team, related_name="current_picks")
	original_owner = models.ForeignKey(Team, related_name="original_picks")
	player = models.ForeignKey(Player, null=True, blank=True)

	class Meta:
		ordering = ["pick_number"]


	def __unicode__(self):
		return self.original_owner.name + "'s " + str(self.draft.year) + " round " + str(self.round) 

	@staticmethod
	def textToPick(year, text):
		try:
			if len(text.split(" ")) > 2:
				[firstname, lastname, pick] = text.split(" ")
				owner = "{} {}".format(firstname, lastname)
			else:
				[owner, pick] = text.split(" ")

			owner = owner.split("'")[0]

			pick = int(pick[0])
		except:
			raise Exception("Could not parse pick: " + text)

		try:
			return DraftPick.objects.get(draft__year=year, original_owner__name=owner, round=pick)
		except:
			raise Exception("Pick " + text + " does not exist")


class FAPickup(models.Model):
	team = models.ForeignKey(Team)
	player = models.CharField(max_length=256)
	player_added = models.ForeignKey(Player,related_name="player_added", null=True, blank=True)
	player_dropped = models.ForeignKey(Player, related_name="player_dropped", null=True, blank=True)
	injured = models.BooleanField()
	date = models.DateTimeField()

	def __unicode__(self):
		return self.team.name + " - " + self.player


class Trade(models.Model):
	teamA = models.ForeignKey(Team, related_name="teamA")
	teamB = models.ForeignKey(Team, related_name="teamB")
	players_received_a = models.ManyToManyField(Player, related_name="players_received_a", blank=True)
	players_received_b = models.ManyToManyField(Player, related_name="players_received_b", blank=True)
	picks_received_a = models.ManyToManyField(DraftPick, related_name="picks_received_a", blank=True)
	picks_received_b = models.ManyToManyField(DraftPick, related_name="picks_received_b", blank=True)
	date = models.DateTimeField()


