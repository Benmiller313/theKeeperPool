# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trade'
        db.create_table(u'teampages_trade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teamA', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teamA', to=orm['teampages.Team'])),
            ('teamB', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teamB', to=orm['teampages.Team'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'teampages', ['Trade'])

        # Adding M2M table for field players_received_a on 'Trade'
        m2m_table_name = db.shorten_name(u'teampages_trade_players_received_a')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trade', models.ForeignKey(orm[u'teampages.trade'], null=False)),
            ('player', models.ForeignKey(orm[u'teampages.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trade_id', 'player_id'])

        # Adding M2M table for field players_received_b on 'Trade'
        m2m_table_name = db.shorten_name(u'teampages_trade_players_received_b')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trade', models.ForeignKey(orm[u'teampages.trade'], null=False)),
            ('player', models.ForeignKey(orm[u'teampages.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trade_id', 'player_id'])

        # Adding M2M table for field picks_received_a on 'Trade'
        m2m_table_name = db.shorten_name(u'teampages_trade_picks_received_a')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trade', models.ForeignKey(orm[u'teampages.trade'], null=False)),
            ('draftpick', models.ForeignKey(orm[u'teampages.draftpick'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trade_id', 'draftpick_id'])

        # Adding M2M table for field picks_received_b on 'Trade'
        m2m_table_name = db.shorten_name(u'teampages_trade_picks_received_b')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trade', models.ForeignKey(orm[u'teampages.trade'], null=False)),
            ('draftpick', models.ForeignKey(orm[u'teampages.draftpick'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trade_id', 'draftpick_id'])

        # Adding model 'DraftPick'
        db.create_table(u'teampages_draftpick', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('round', self.gf('django.db.models.fields.IntegerField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owner', to=orm['teampages.Team'])),
            ('original_owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='original_owner', to=orm['teampages.Team'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teampages.Player'], null=True)),
        ))
        db.send_create_signal(u'teampages', ['DraftPick'])


    def backwards(self, orm):
        # Deleting model 'Trade'
        db.delete_table(u'teampages_trade')

        # Removing M2M table for field players_received_a on 'Trade'
        db.delete_table(db.shorten_name(u'teampages_trade_players_received_a'))

        # Removing M2M table for field players_received_b on 'Trade'
        db.delete_table(db.shorten_name(u'teampages_trade_players_received_b'))

        # Removing M2M table for field picks_received_a on 'Trade'
        db.delete_table(db.shorten_name(u'teampages_trade_picks_received_a'))

        # Removing M2M table for field picks_received_b on 'Trade'
        db.delete_table(db.shorten_name(u'teampages_trade_picks_received_b'))

        # Deleting model 'DraftPick'
        db.delete_table(u'teampages_draftpick')


    models = {
        u'teampages.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Team']"}),
            'trophy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Trophy']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teampages.draftpick': {
            'Meta': {'object_name': 'DraftPick'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'original_owner'", 'to': u"orm['teampages.Team']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': u"orm['teampages.Team']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teampages.Player']", 'null': 'True'}),
            'round': ('django.db.models.fields.IntegerField', [], {}),
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
        u'teampages.trade': {
            'Meta': {'object_name': 'Trade'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picks_received_a': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'picks_received_a'", 'symmetrical': 'False', 'to': u"orm['teampages.DraftPick']"}),
            'picks_received_b': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'picks_received_b'", 'symmetrical': 'False', 'to': u"orm['teampages.DraftPick']"}),
            'players_received_a': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'players_received_a'", 'symmetrical': 'False', 'to': u"orm['teampages.Player']"}),
            'players_received_b': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'players_received_b'", 'symmetrical': 'False', 'to': u"orm['teampages.Player']"}),
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