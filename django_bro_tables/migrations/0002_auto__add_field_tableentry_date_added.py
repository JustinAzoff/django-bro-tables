# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TableEntry.date_added'
        db.add_column(u'django_bro_tables_tableentry', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 11, 20, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TableEntry.date_added'
        db.delete_column(u'django_bro_tables_tableentry', 'date_added')


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
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['django_bro_tables.Table']"})
        }
    }

    complete_apps = ['django_bro_tables']