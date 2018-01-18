# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stat.point_delta'
        db.add_column(u'teampages_stat', 'point_delta',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stat.point_delta'
        db.delete_column(u'teampages_stat', 'point_delta')


    models = {
        u'teampages.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Team']"}),
            'trophy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Trophy']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teampages.draft': {
            'Meta': {'object_name': 'Draft'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teampages.Team']", 'through': u"orm['teampages.DraftOrder']", 'symmetrical': 'False'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teampages.draftorder': {
            'Meta': {'object_name': 'DraftOrder'},
            'draft': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Draft']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Team']"})
        },
        u'teampages.draftpick': {
            'Meta': {'ordering': "['pick_number']", 'object_name': 'DraftPick'},
            'draft': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Draft']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'original_picks'", 'to': u"orm['teampages.Team']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'current_picks'", 'to': u"orm['teampages.Team']"}),
            'pick_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Player']", 'null': 'True', 'blank': 'True'}),
            'round': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teampages.fapickup': {
            'Meta': {'object_name': 'FAPickup'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injured': ('django.db.models.fields.BooleanField', [], {}),
            'player': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'player_added': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'player_added'", 'null': 'True', 'to': u"orm['teampages.Player']"}),
            'player_dropped': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'player_dropped'", 'null': 'True', 'to': u"orm['teampages.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Team']"})
        },
        u'teampages.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'in_waivers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nhl_team': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['teampages.Team']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'salary': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teampages.stat': {
            'Meta': {'object_name': 'Stat'},
            'assists': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game_winning_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'games_played': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ot_loss': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Player']"}),
            'plus_minus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'point_delta': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_handed_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'shutouts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'teampages.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascot_image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'teampages.trade': {
            'Meta': {'object_name': 'Trade'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picks_received_a': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'picks_received_a'", 'blank': 'True', 'to': u"orm['teampages.DraftPick']"}),
            'picks_received_b': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'picks_received_b'", 'blank': 'True', 'to': u"orm['teampages.DraftPick']"}),
            'players_received_a': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'players_received_a'", 'blank': 'True', 'to': u"orm['teampages.Player']"}),
            'players_received_b': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'players_received_b'", 'blank': 'True', 'to': u"orm['teampages.Player']"}),
            'teamA': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teamA'", 'to': u"orm['teampages.Team']"}),
            'teamB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teamB'", 'to': u"orm['teampages.Team']"})
        },
        u'teampages.trophy': {
            'Meta': {'object_name': 'Trophy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['teampages']