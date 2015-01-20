from django.contrib import admin

from teampages.models import Team, Trophy, Banner, FAPickup, Player

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline

class PlayerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Player, PlayerAdmin)

class FAPickupAdmin(AjaxSelectAdmin):
	form = make_ajax_form(FAPickup, {
		'player_added':'player',
		'player_dropped': 'player',
		})
admin.site.register(FAPickup, FAPickupAdmin)


admin.site.register(Team)
admin.site.register(Trophy)
admin.site.register(Banner)
