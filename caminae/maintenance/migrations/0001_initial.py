# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Intervention'
        db.create_table('interventions', (
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('intervention_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('in_maintenance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('width', self.gf('django.db.models.fields.FloatField')()),
            ('height', self.gf('django.db.models.fields.FloatField')()),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('slope', self.gf('django.db.models.fields.IntegerField')()),
            ('material_cost', self.gf('django.db.models.fields.FloatField')()),
            ('heliport_cost', self.gf('django.db.models.fields.FloatField')()),
            ('subcontract_cost', self.gf('django.db.models.fields.FloatField')()),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stake', self.gf('django.db.models.fields.related.ForeignKey')(related_name='interventions', null=True, to=orm['core.Stake'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.InterventionStatus'])),
            ('typology', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.InterventionTypology'], null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.Project'], null=True, blank=True)),
        ))
        db.send_create_signal('maintenance', ['Intervention'])

        # Adding M2M table for field topologies on 'Intervention'
        db.create_table('interventions_topologies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('intervention', models.ForeignKey(orm['maintenance.intervention'], null=False)),
            ('topologymixin', models.ForeignKey(orm['core.topologymixin'], null=False))
        ))
        db.create_unique('interventions_topologies', ['intervention_id', 'topologymixin_id'])

        # Adding M2M table for field disorders on 'Intervention'
        db.create_table('interventions_disorders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('intervention', models.ForeignKey(orm['maintenance.intervention'], null=False)),
            ('interventiondisorder', models.ForeignKey(orm['maintenance.interventiondisorder'], null=False))
        ))
        db.create_unique('interventions_disorders', ['intervention_id', 'interventiondisorder_id'])

        # Adding model 'InterventionStatus'
        db.create_table('bib_de_suivi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionStatus'])

        # Adding model 'InterventionTypology'
        db.create_table('typologie_des_interventions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('typology', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionTypology'])

        # Adding model 'InterventionDisorder'
        db.create_table('desordres', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('disorder', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionDisorder'])

        # Adding model 'InterventionJob'
        db.create_table('bib_fonctions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('job', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionJob'])

        # Adding model 'ManDay'
        db.create_table('journeeshomme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nb_days', self.gf('django.db.models.fields.IntegerField')()),
            ('intervention', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.Intervention'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.InterventionJob'])),
        ))
        db.send_create_signal('maintenance', ['ManDay'])

        # Adding model 'Project'
        db.create_table('chantiers', (
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('project_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('begin_year', self.gf('django.db.models.fields.IntegerField')()),
            ('end_year', self.gf('django.db.models.fields.IntegerField')()),
            ('constraint', self.gf('django.db.models.fields.TextField')()),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project_owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='own', to=orm['common.Organism'])),
            ('project_manager', self.gf('django.db.models.fields.related.ForeignKey')(related_name='manage', to=orm['common.Organism'])),
        ))
        db.send_create_signal('maintenance', ['Project'])

        # Adding M2M table for field contractors on 'Project'
        db.create_table('chantiers_contractors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['maintenance.project'], null=False)),
            ('contractor', models.ForeignKey(orm['maintenance.contractor'], null=False))
        ))
        db.create_unique('chantiers_contractors', ['project_id', 'contractor_id'])

        # Adding model 'Contractor'
        db.create_table('prestataires', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('contractor', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['Contractor'])

        # Adding model 'Funding'
        db.create_table('financement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.Project'])),
            ('organism', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Organism'])),
        ))
        db.send_create_signal('maintenance', ['Funding'])


    def backwards(self, orm):
        # Deleting model 'Intervention'
        db.delete_table('interventions')

        # Removing M2M table for field topologies on 'Intervention'
        db.delete_table('interventions_topologies')

        # Removing M2M table for field disorders on 'Intervention'
        db.delete_table('interventions_disorders')

        # Deleting model 'InterventionStatus'
        db.delete_table('bib_de_suivi')

        # Deleting model 'InterventionTypology'
        db.delete_table('typologie_des_interventions')

        # Deleting model 'InterventionDisorder'
        db.delete_table('desordres')

        # Deleting model 'InterventionJob'
        db.delete_table('bib_fonctions')

        # Deleting model 'ManDay'
        db.delete_table('journeeshomme')

        # Deleting model 'Project'
        db.delete_table('chantiers')

        # Removing M2M table for field contractors on 'Project'
        db.delete_table('chantiers_contractors')

        # Deleting model 'Contractor'
        db.delete_table('prestataires')

        # Deleting model 'Funding'
        db.delete_table('financement')


    models = {
        'authent.structure': {
            'Meta': {'object_name': 'Structure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'common.organism': {
            'Meta': {'object_name': 'Organism', 'db_table': "'liste_de_tous_les_organismes'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organism': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'core.datasource': {
            'Meta': {'object_name': 'Datasource', 'db_table': "'source_donnees'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'core.network': {
            'Meta': {'object_name': 'Network', 'db_table': "'reseau'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'core.path': {
            'Meta': {'object_name': 'Path', 'db_table': "'troncons'"},
            'ascent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'denivelee_positive'"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'remarques'"}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'to': "orm['core.Datasource']"}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {}),
            'descent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'denivelee_negative'"}),
            'geom': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '2154', 'spatial_index': 'False'}),
            'geom_cadastre': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '2154', 'null': 'True', 'spatial_index': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0', 'db_column': "'longueur'"}),
            'max_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'altitude_maximum'"}),
            'min_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'altitude_minimum'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "'nom_troncon'"}),
            'networks': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.Network']"}),
            'stake': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'to': "orm['core.Stake']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"}),
            'trail': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'to': "orm['core.Trail']"}),
            'usages': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.Usage']"}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'troncon_valide'"})
        },
        'core.pathaggregation': {
            'Meta': {'object_name': 'PathAggregation', 'db_table': "'evenements_troncons'"},
            'end_position': ('django.db.models.fields.FloatField', [], {'db_column': "'pk_fin'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Path']", 'db_column': "'troncon'"}),
            'start_position': ('django.db.models.fields.FloatField', [], {'db_column': "'pk_debut'"}),
            'topo_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.TopologyMixin']", 'db_column': "'evenement'"})
        },
        'core.stake': {
            'Meta': {'object_name': 'Stake', 'db_table': "'enjeu'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stake': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'core.topologymixin': {
            'Meta': {'object_name': 'TopologyMixin', 'db_table': "'evenements'"},
            'date_insert': ('django.db.models.fields.DateTimeField', [], {}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'supprime'"}),
            'geom': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '2154', 'spatial_index': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.TopologyMixinKind']"}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0', 'db_column': "'longueur'"}),
            'offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'decallage'"}),
            'troncons': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Path']", 'through': "orm['core.PathAggregation']", 'symmetrical': 'False'})
        },
        'core.topologymixinkind': {
            'Meta': {'object_name': 'TopologyMixinKind', 'db_table': "'type_evenements'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'core.trail': {
            'Meta': {'object_name': 'Trail', 'db_table': "'sentier'"},
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'core.usage': {
            'Meta': {'object_name': 'Usage', 'db_table': "'usage'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usage': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'maintenance.contractor': {
            'Meta': {'object_name': 'Contractor', 'db_table': "'prestataires'"},
            'contractor': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.funding': {
            'Meta': {'object_name': 'Funding', 'db_table': "'financement'"},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organism': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Organism']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.Project']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.intervention': {
            'Meta': {'object_name': 'Intervention', 'db_table': "'interventions'"},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'disorders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'interventions'", 'symmetrical': 'False', 'to': "orm['maintenance.InterventionDisorder']"}),
            'height': ('django.db.models.fields.FloatField', [], {}),
            'heliport_cost': ('django.db.models.fields.FloatField', [], {}),
            'in_maintenance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'intervention_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['maintenance.InterventionJob']", 'through': "orm['maintenance.ManDay']", 'symmetrical': 'False'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'material_cost': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.Project']", 'null': 'True', 'blank': 'True'}),
            'slope': ('django.db.models.fields.IntegerField', [], {}),
            'stake': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interventions'", 'null': 'True', 'to': "orm['core.Stake']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.InterventionStatus']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"}),
            'subcontract_cost': ('django.db.models.fields.FloatField', [], {}),
            'topologies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'interventions'", 'symmetrical': 'False', 'to': "orm['core.TopologyMixin']"}),
            'typology': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.InterventionTypology']", 'null': 'True', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.FloatField', [], {})
        },
        'maintenance.interventiondisorder': {
            'Meta': {'object_name': 'InterventionDisorder', 'db_table': "'desordres'"},
            'disorder': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.interventionjob': {
            'Meta': {'object_name': 'InterventionJob', 'db_table': "'bib_fonctions'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.interventionstatus': {
            'Meta': {'object_name': 'InterventionStatus', 'db_table': "'bib_de_suivi'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.interventiontypology': {
            'Meta': {'object_name': 'InterventionTypology', 'db_table': "'typologie_des_interventions'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"}),
            'typology': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'maintenance.manday': {
            'Meta': {'object_name': 'ManDay', 'db_table': "'journeeshomme'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervention': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.Intervention']"}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.InterventionJob']"}),
            'nb_days': ('django.db.models.fields.IntegerField', [], {})
        },
        'maintenance.project': {
            'Meta': {'object_name': 'Project', 'db_table': "'chantiers'"},
            'begin_year': ('django.db.models.fields.IntegerField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'constraint': ('django.db.models.fields.TextField', [], {}),
            'contractors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['maintenance.Contractor']"}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_year': ('django.db.models.fields.IntegerField', [], {}),
            'founders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['common.Organism']", 'through': "orm['maintenance.Funding']", 'symmetrical': 'False'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'project_manager': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manage'", 'to': "orm['common.Organism']"}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'own'", 'to': "orm['common.Organism']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['maintenance']