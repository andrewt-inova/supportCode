# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductSuite'
        db.create_table(u'products_productsuite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'products', ['ProductSuite'])

        # Deleting field 'Product.prodType'
        db.delete_column(u'products_product', 'prodType')

        # Adding field 'Product.product_type'
        db.add_column(u'products_product', 'product_type',
                      self.gf('django.db.models.fields.CharField')(default='Software', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ProductSuite'
        db.delete_table(u'products_productsuite')

        # Adding field 'Product.prodType'
        db.add_column(u'products_product', 'prodType',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 2, 20, 0, 0), max_length=20),
                      keep_default=False)

        # Deleting field 'Product.product_type'
        db.delete_column(u'products_product', 'product_type')


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
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'products.productsuite': {
            'Meta': {'object_name': 'ProductSuite'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['products']