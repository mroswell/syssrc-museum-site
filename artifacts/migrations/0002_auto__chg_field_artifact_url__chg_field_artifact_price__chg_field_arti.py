# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Artifact.url'
        db.alter_column(u'artifacts_artifact', 'url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Artifact.price'
        db.alter_column(u'artifacts_artifact', 'price', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Artifact.title'
        db.alter_column(u'artifacts_artifact', 'title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Artifact.description'
        db.alter_column(u'artifacts_artifact', 'description', self.gf('django.db.models.fields.CharField')(max_length=8000, null=True))

    def backwards(self, orm):

        # Changing field 'Artifact.url'
        db.alter_column(u'artifacts_artifact', 'url', self.gf('django.db.models.fields.CharField')(default='http://www.syssrc.com', max_length=200))

        # Changing field 'Artifact.price'
        db.alter_column(u'artifacts_artifact', 'price', self.gf('django.db.models.fields.CharField')(default=0, max_length=200))

        # Changing field 'Artifact.title'
        db.alter_column(u'artifacts_artifact', 'title', self.gf('django.db.models.fields.CharField')(default='What is this', max_length=200))

        # Changing field 'Artifact.description'
        db.alter_column(u'artifacts_artifact', 'description', self.gf('django.db.models.fields.CharField')(default='description', max_length=8000))

    models = {
        u'artifacts.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '8000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://www.syssrc.com'", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['artifacts']