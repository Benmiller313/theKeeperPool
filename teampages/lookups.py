from ajax_select import LookupChannel
from django.utils.html import escape
from django.db.models import Q
from teampages.models import *


class PlayerByName(LookupChannel):

	model = Player

	def get_query(self, q, request):
		return Player.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))

	def get_result(self,obj):
		""" result is the simple text that is the completion of what the person typed """
		return obj.fullName()

	def format_match(self,obj):
		""" (HTML) formatted item for display in the dropdown """
		return self.format_item_display(obj)

	def format_item_display(self,obj):
		""" (HTML) formatted item for displaying item in the selected deck area """
		team = obj.owner if obj.owner else "Free Agent" 
		return u"%s<div><i>%s</i></div>" % (escape(obj.fullName()),escape(team))

	def check_auth(self, request):
		pass