# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Requirement'
        db.create_table(u'products_requirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('processor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ram', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hard_disk', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('network', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('other', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('product', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Product'], unique=True)),
        ))
        db.send_create_signal(u'products', ['Requirement'])


    def backwards(self, orm):
        # Deleting model 'Requirement'
        db.delete_table(u'products_requirement')


    models = {
        u'products.faq': {
            'Meta': {'ordering': "('question',)", 'object_name': 'FAQ'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Product']", 'symmetrical': 'False'}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        },
        u'products.product': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Product'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product_suite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.ProductSuite']", 'null': 'True'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'products.productsuite': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ProductSuite'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'products.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'hard_disk': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'other': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'processor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['products.Product']", 'unique': 'True'}),
            'ram': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['products']