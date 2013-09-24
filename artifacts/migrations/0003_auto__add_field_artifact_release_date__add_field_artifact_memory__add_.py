# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artifact.release_date'
        db.add_column(u'artifacts_artifact', 'release_date',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.memory'
        db.add_column(u'artifacts_artifact', 'memory',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.cpu'
        db.add_column(u'artifacts_artifact', 'cpu',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.display'
        db.add_column(u'artifacts_artifact', 'display',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.storage'
        db.add_column(u'artifacts_artifact', 'storage',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artifact.ports'
        db.add_column(u'artifacts_artifact', 'ports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artifact.release_date'
        db.delete_column(u'artifacts_artifact', 'release_date')

        # Deleting field 'Artifact.memory'
        db.delete_column(u'artifacts_artifact', 'memory')

        # Deleting field 'Artifact.cpu'
        db.delete_column(u'artifacts_artifact', 'cpu')

        # Deleting field 'Artifact.display'
        db.delete_column(u'artifacts_artifact', 'display')

        # Deleting field 'Artifact.storage'
        db.delete_column(u'artifacts_artifact', 'storage')

        # Deleting field 'Artifact.ports'
        db.delete_column(u'artifacts_artifact', 'ports')


    models = {
        u'artifacts.artifact': {
            'Meta': {'object_name': 'Artifact'},
            'cpu': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '8000', 'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memory': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'storage': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'http://www.syssrc.com'", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['artifacts']