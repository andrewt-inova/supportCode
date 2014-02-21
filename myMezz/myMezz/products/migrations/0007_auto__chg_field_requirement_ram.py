# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Requirement.ram'
        db.alter_column(u'products_requirement', 'ram', self.gf('django.db.models.fields.IntegerField')(max_length='2'))

    def backwards(self, orm):

        # Changing field 'Requirement.ram'
        db.alter_column(u'products_requirement', 'ram', self.gf('django.db.models.fields.IntegerField')(max_length=2))

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
            'Meta': {'ordering': "('product',)", 'object_name': 'Requirement'},
            'hard_disk': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'other': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'processor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['products.ProductSuite']", 'unique': 'True'}),
            'ram': ('django.db.models.fields.IntegerField', [], {'default': "'2'", 'max_length': "'2'"})
        }
    }

    complete_apps = ['products']