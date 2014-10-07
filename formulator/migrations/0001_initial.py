# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Form'
        db.create_table(u'formulator_form', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('form_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('form_action', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('form_method', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10)),
            ('form_id', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=u'name', unique_with=())),
            ('form_class', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('form_accept_charset', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('form_autocomplete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('form_novalidate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('form_enctype', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('form_target', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('attrs', self.gf(u'django_hstore.fields.DictionaryField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'formulator', ['Form'])

        # Adding model 'FieldSet'
        db.create_table(u'formulator_fieldset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formulator.Form'])),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('legend', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'formulator', ['FieldSet'])

        # Adding model 'Field'
        db.create_table(u'formulator_field', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('formset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['formulator.FieldSet'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('attrs', self.gf(u'django_hstore.fields.DictionaryField')(null=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=u'name', unique_with=())),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('widget', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('initial', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('help_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('show_hidden_initial', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'formulator', ['Field'])


    def backwards(self, orm):
        # Deleting model 'Form'
        db.delete_table(u'formulator_form')

        # Deleting model 'FieldSet'
        db.delete_table(u'formulator_fieldset')

        # Deleting model 'Field'
        db.delete_table(u'formulator_field')


    models = {
        u'formulator.field': {
            'Meta': {'ordering': "[u'position']", 'object_name': 'Field'},
            'attrs': (u'django_hstore.fields.DictionaryField', [], {'null': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'formset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['formulator.FieldSet']"}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_hidden_initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "u'name'", 'unique_with': '()'}),
            'widget': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'formulator.fieldset': {
            'Meta': {'object_name': 'FieldSet'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['formulator.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legend': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        u'formulator.form': {
            'Meta': {'object_name': 'Form'},
            'attrs': (u'django_hstore.fields.DictionaryField', [], {'null': 'True', 'blank': 'True'}),
            'form_accept_charset': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'form_action': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'form_autocomplete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form_class': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'form_enctype': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'form_id': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "u'name'", 'unique_with': '()'}),
            'form_method': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10'}),
            'form_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'form_novalidate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form_target': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['formulator']