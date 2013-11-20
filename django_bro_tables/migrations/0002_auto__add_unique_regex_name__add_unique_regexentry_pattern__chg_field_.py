# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Regex', fields ['name']
        db.create_unique(u'django_bro_tables_regex', ['name'])

        # Adding unique constraint on 'RegexEntry', fields ['pattern']
        db.create_unique(u'django_bro_tables_regexentry', ['pattern'])


        # Changing field 'RegexEntry.date_added'
        db.alter_column(u'django_bro_tables_regexentry', 'date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):
        # Removing unique constraint on 'RegexEntry', fields ['pattern']
        db.delete_unique(u'django_bro_tables_regexentry', ['pattern'])

        # Removing unique constraint on 'Regex', fields ['name']
        db.delete_unique(u'django_bro_tables_regex', ['name'])


        # Changing field 'RegexEntry.date_added'
        db.alter_column(u'django_bro_tables_regexentry', 'date_added', self.gf('django.db.models.fields.DateTimeField')())

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
        }
    }

    complete_apps = ['django_bro_tables']