# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'main_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('CIAWFB_name_short', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Country'])

        # Adding model 'CIAWFBEntry'
        db.create_table(u'main_ciawfbentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Country'])),
            ('date_entered', self.gf('django.db.models.fields.DateField')()),
            ('agriculture_products', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('country_name_long', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('background', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('climate', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('terrain', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('annual_renewable_water_resources_cu_km', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('annual_freshwater_withdrawal_cu_km', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('natural_hazards', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('environment_current_issues', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('total_population_life_expectancy_at_birth', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('HIVAIDS_adult_prevalance_rate_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('economic_narrative', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('GDP_real_growth_rate_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('public_debt_as_percentage_of_GDP', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('consumer_prices_inflation_rate_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'main', ['CIAWFBEntry'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'main_country')

        # Deleting model 'CIAWFBEntry'
        db.delete_table(u'main_ciawfbentry')


    models = {
        u'main.ciawfbentry': {
            'GDP_real_growth_rate_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'HIVAIDS_adult_prevalance_rate_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'Meta': {'object_name': 'CIAWFBEntry'},
            'agriculture_products': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'annual_freshwater_withdrawal_cu_km': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'annual_renewable_water_resources_cu_km': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'background': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'climate': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'consumer_prices_inflation_rate_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Country']"}),
            'country_name_long': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_entered': ('django.db.models.fields.DateField', [], {}),
            'economic_narrative': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'environment_current_issues': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_hazards': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'public_debt_as_percentage_of_GDP': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'terrain': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'total_population_life_expectancy_at_birth': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        },
        u'main.country': {
            'CIAWFB_name_short': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']