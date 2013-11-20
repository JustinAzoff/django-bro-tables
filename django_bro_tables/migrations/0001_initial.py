# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Regex'
        db.create_table(u'django_bro_tables_regex', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'django_bro_tables', ['Regex'])

        # Adding model 'RegexEntry'
        db.create_table(u'django_bro_tables_regexentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('regex', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['django_bro_tables.Regex'])),
            ('pattern', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('flags', self.gf('django.db.models.fields.CharField')(default='e', max_length=10)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'django_bro_tables', ['RegexEntry'])

        # Adding model 'Table'
        db.create_table(u'django_bro_tables_table', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('num_fields', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('fields', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'django_bro_tables', ['Table'])

        # Adding model 'TableEntry'
        db.create_table(u'django_bro_tables_tableentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('table', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['django_bro_tables.Table'])),
            ('c0', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('c1', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('c2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('c3', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('c4', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('c5', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'django_bro_tables', ['TableEntry'])


    def backwards(self, orm):
        # Deleting model 'Regex'
        db.delete_table(u'django_bro_tables_regex')

        # Deleting model 'RegexEntry'
        db.delete_table(u'django_bro_tables_regexentry')

        # Deleting model 'Table'
        db.delete_table(u'django_bro_tables_table')

        # Deleting model 'TableEntry'
        db.delete_table(u'django_bro_tables_tableentry')


    models = {
        u'django_bro_tables.regex': {
            'Meta': {'object_name': 'Regex'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'django_bro_tables.regexentry': {
            'Meta': {'object_name': 'RegexEntry'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flags': ('django.db.models.fields.CharField', [], {'default': "'e'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pattern': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'regex': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['django_bro_tables.Regex']"})
        },
        u'django_bro_tables.table': {
            'Meta': {'object_name': 'Table'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fields': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'num_fields': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'django_bro_tables.tableentry': {
            'Meta': {'object_name': 'TableEntry'},
            'c0': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'c1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'c2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'c3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'c4': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'c5': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['django_bro_tables.Table']"})
        }
    }

    complete_apps = ['django_bro_tables']