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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'django_bro_tables', ['Regex'])

        # Adding model 'RegexEntry'
        db.create_table(u'django_bro_tables_regexentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('regex', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_bro_tables.Regex'])),
            ('pattern', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('flags', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'django_bro_tables', ['RegexEntry'])


    def backwards(self, orm):
        # Deleting model 'Regex'
        db.delete_table(u'django_bro_tables_regex')

        # Deleting model 'RegexEntry'
        db.delete_table(u'django_bro_tables_regexentry')


    models = {
        u'django_bro_tables.regex': {
            'Meta': {'object_name': 'Regex'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_bro_tables.regexentry': {
            'Meta': {'object_name': 'RegexEntry'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flags': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'regex': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_bro_tables.Regex']"})
        }
    }

    complete_apps = ['django_bro_tables']