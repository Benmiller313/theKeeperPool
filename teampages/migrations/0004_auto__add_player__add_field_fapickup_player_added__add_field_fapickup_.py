# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'teampages_player', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('salary', self.gf('django.db.models.fields.IntegerField')()),
            ('nhl_team', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['teampages.Team'], null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('in_waivers', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'teampages', ['Player'])

        # Adding field 'FAPickup.player_added'
        db.add_column(u'teampages_fapickup', 'player_added',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='player_added', to=orm['teampages.Player']),
                      keep_default=False)

        # Adding field 'FAPickup.player_dropped'
        db.add_column(u'teampages_fapickup', 'player_dropped',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='player_dropped', to=orm['teampages.Player']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'teampages_player')

        # Deleting field 'FAPickup.player_added'
        db.delete_column(u'teampages_fapickup', 'player_added_id')

        # Deleting field 'FAPickup.player_dropped'
        db.delete_column(u'teampages_fapickup', 'player_dropped_id')


    models = {
        u'teampages.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Team']"}),
            'trophy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Trophy']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teampages.fapickup': {
            'Meta': {'object_name': 'FAPickup'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injured': ('django.db.models.fields.BooleanField', [], {}),
            'player': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'player_added': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_added'", 'to': u"orm['teampages.Player']"}),
            'player_dropped': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_dropped'", 'to': u"orm['teampages.Player']"}),
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
        u'teampages.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascot_image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'teampages.trophy': {
            'Meta': {'object_name': 'Trophy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['teampages']