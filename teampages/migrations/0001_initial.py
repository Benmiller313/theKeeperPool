# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'teampages_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('mascot_image', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'teampages', ['Team'])

        # Adding model 'Trophy'
        db.create_table(u'teampages_trophy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'teampages', ['Trophy'])

        # Adding model 'Banner'
        db.create_table(u'teampages_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trophy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teampages.Trophy'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teampages.Team'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'teampages', ['Banner'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'teampages_team')

        # Deleting model 'Trophy'
        db.delete_table(u'teampages_trophy')

        # Deleting model 'Banner'
        db.delete_table(u'teampages_banner')


    models = {
        u'teampages.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Team']"}),
            'trophy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Trophy']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
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