from django.contrib import admin

from teampages.models import Team, Trophy, Banner, FAPickup, Player, Trade, DraftPick

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

admin.site.register(Trade, TradeAdmin)

admin.site.register(Team)
admin.site.register(Trophy)
admin.site.register(Banner)
admin.site.register(DraftPick)