# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table('recrep_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60, db_index=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('accnum', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('balance', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('recrep', ['Account'])

        # Adding model 'Voucher'
        db.create_table('recrep_voucher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.CharField')(max_length=60, db_index=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_used', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('Account', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='Account', null=True, blank=True, to=orm['recrep.Account'])),
        ))
        db.send_create_signal('recrep', ['Voucher'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table('recrep_account')

        # Deleting model 'Voucher'
        db.delete_table('recrep_voucher')


    models = {
        'recrep.account': {
            'Meta': {'object_name': 'Account'},
            'accnum': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'balance': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_index': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'recrep.voucher': {
            'Account': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'Account'", 'null': 'True', 'blank': 'True', 'to': "orm['recrep.Account']"}),
            'Meta': {'object_name': 'Voucher'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date_used': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_index': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['recrep']