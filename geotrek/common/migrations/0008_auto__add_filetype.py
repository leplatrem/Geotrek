# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, connection

from geotrek.authent.models import default_structure


class Migration(SchemaMigration):

    def forwards(self, orm):
        exists = 'fl_b_fichier' in connection.introspection.table_names()
        if exists:
            # Table exists, just add column.
            db.add_column('fl_b_fichier', 'structure',
                          self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'], db_column='structure', default=default_structure().pk),
                          keep_default=False)
        else:
            db.create_table('fl_b_fichier', (
                ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('type', self.gf('django.db.models.fields.CharField')(max_length=128)),
                ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'], db_column='structure')),
            ))
            db.send_create_signal('common', ['FileType'])

    def backwards(self, orm):
        # Deleting model 'FileType'
        db.delete_table('fl_b_fichier')

    models = {
        'authent.structure': {
            'Meta': {'ordering': "['name']", 'object_name': 'Structure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'common.filetype': {
            'Meta': {'ordering': "['type']", 'object_name': 'FileType', 'db_table': "'fl_b_fichier'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']", 'db_column': "'structure'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'common.organism': {
            'Meta': {'ordering': "['organism']", 'object_name': 'Organism', 'db_table': "'m_b_organisme'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organism': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'organisme'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']", 'db_column': "'structure'"})
        }
    }

    complete_apps = ['common']