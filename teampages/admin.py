from django.contrib import admin
from django.conf.urls import patterns

from teampages.models import Team, Trophy, Banner, FAPickup, Player, Trade, DraftPick, Draft, DraftOrder

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline

class PlayerAdmin(admin.ModelAdmin):
	list_filter=("owner", )
	search_fields=["first_name", "last_name"]

admin.site.register(Player, PlayerAdmin)

class FAPickupAdmin(AjaxSelectAdmin):
	form = make_ajax_form(FAPickup, {
		'player_added':'player',
		'player_dropped': 'player',
		})
admin.site.register(FAPickup, FAPickupAdmin)

class TradeAdmin(AjaxSelectAdmin):
	form = make_ajax_form(Trade, {
			'players_received_a':'player', 
			'players_received_b': 'player',
		})


class DraftOrderInline(admin.TabularInline):
	model = DraftOrder
	extra = 8

class DraftPickInline(admin.TabularInline):
	model = DraftPick
	extra = 3

class DraftAdmin(admin.ModelAdmin):

	change_form_template = "teampages/change_form.html"

	inlines = [DraftOrderInline, DraftPickInline]

	def get_urls(self):
		urls = super(DraftAdmin, self).get_urls()
		my_urls = patterns('',
		    (r'^(.+)/bulk_draft/$', self.bulk_draft)
		)
		return my_urls + urls

	def bulk_draft(self, request, id):
		# custom view which should return an HttpResponse
		pass
admin.site.register(Trade, TradeAdmin)

admin.site.register(Team)
admin.site.register(Trophy)
admin.site.register(Banner)
admin.site.register(DraftPick)
admin.site.register(Draft, DraftAdmin)
