# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artifact'
        db.create_table(u'artifacts_artifact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=8000)),
        ))
        db.send_create_signal(u'artifacts', ['Artifact'])


    def backwards(self, orm):
        # Deleting model 'Artifact'
        db.delete_table(u'artifacts_artifact')


    models = {
        u'artifacts.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['artifacts']