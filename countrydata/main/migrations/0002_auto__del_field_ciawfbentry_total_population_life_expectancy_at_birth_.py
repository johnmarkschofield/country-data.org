# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CIAWFBEntry.total_population_life_expectancy_at_birth'
        db.delete_column(u'main_ciawfbentry', 'total_population_life_expectancy_at_birth')

        # Deleting field 'CIAWFBEntry.annual_freshwater_withdrawal_cu_km'
        db.delete_column(u'main_ciawfbentry', 'annual_freshwater_withdrawal_cu_km')

        # Deleting field 'CIAWFBEntry.GDP_real_growth_rate_percentage'
        db.delete_column(u'main_ciawfbentry', 'GDP_real_growth_rate_percentage')

        # Deleting field 'CIAWFBEntry.HIVAIDS_adult_prevalance_rate_percent'
        db.delete_column(u'main_ciawfbentry', 'HIVAIDS_adult_prevalance_rate_percent')

        # Deleting field 'CIAWFBEntry.public_debt_as_percentage_of_GDP'
        db.delete_column(u'main_ciawfbentry', 'public_debt_as_percentage_of_GDP')

        # Deleting field 'CIAWFBEntry.annual_renewable_water_resources_cu_km'
        db.delete_column(u'main_ciawfbentry', 'annual_renewable_water_resources_cu_km')

        # Deleting field 'CIAWFBEntry.economic_narrative'
        db.delete_column(u'main_ciawfbentry', 'economic_narrative')

        # Deleting field 'CIAWFBEntry.country_name_long'
        db.delete_column(u'main_ciawfbentry', 'country_name_long')

        # Deleting field 'CIAWFBEntry.consumer_prices_inflation_rate_percent'
        db.delete_column(u'main_ciawfbentry', 'consumer_prices_inflation_rate_percent')

        # Adding field 'CIAWFBEntry.administrative_divisions'
        db.add_column(u'main_ciawfbentry', 'administrative_divisions',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.age_structure'
        db.add_column(u'main_ciawfbentry', 'age_structure',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.airports'
        db.add_column(u'main_ciawfbentry', 'airports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.airports_with_paved_runways'
        db.add_column(u'main_ciawfbentry', 'airports_with_paved_runways',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.airports_with_unpaved_runways'
        db.add_column(u'main_ciawfbentry', 'airports_with_unpaved_runways',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.area'
        db.add_column(u'main_ciawfbentry', 'area',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.area_comparative'
        db.add_column(u'main_ciawfbentry', 'area_comparative',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.birth_rate'
        db.add_column(u'main_ciawfbentry', 'birth_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.broadcast_media'
        db.add_column(u'main_ciawfbentry', 'broadcast_media',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.budget'
        db.add_column(u'main_ciawfbentry', 'budget',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.budget_surplus_or_deficit'
        db.add_column(u'main_ciawfbentry', 'budget_surplus_or_deficit',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.capital'
        db.add_column(u'main_ciawfbentry', 'capital',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.carbon_dioxide_emissions_from_consumption_of_energy'
        db.add_column(u'main_ciawfbentry', 'carbon_dioxide_emissions_from_consumption_of_energy',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.central_bank_discount_rate'
        db.add_column(u'main_ciawfbentry', 'central_bank_discount_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.children_under_the_age_of_5_years_underweight'
        db.add_column(u'main_ciawfbentry', 'children_under_the_age_of_5_years_underweight',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.coastline'
        db.add_column(u'main_ciawfbentry', 'coastline',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.commercial_bank_prime_lending_rate'
        db.add_column(u'main_ciawfbentry', 'commercial_bank_prime_lending_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.communications_note'
        db.add_column(u'main_ciawfbentry', 'communications_note',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.constitution'
        db.add_column(u'main_ciawfbentry', 'constitution',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.country_name'
        db.add_column(u'main_ciawfbentry', 'country_name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.crude_oil_exports'
        db.add_column(u'main_ciawfbentry', 'crude_oil_exports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.crude_oil_imports'
        db.add_column(u'main_ciawfbentry', 'crude_oil_imports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.crude_oil_production'
        db.add_column(u'main_ciawfbentry', 'crude_oil_production',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.crude_oil_proved_reserves'
        db.add_column(u'main_ciawfbentry', 'crude_oil_proved_reserves',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.current_account_balance'
        db.add_column(u'main_ciawfbentry', 'current_account_balance',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.death_rate'
        db.add_column(u'main_ciawfbentry', 'death_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.debt_external'
        db.add_column(u'main_ciawfbentry', 'debt_external',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.demographic_profile'
        db.add_column(u'main_ciawfbentry', 'demographic_profile',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.dependency_status'
        db.add_column(u'main_ciawfbentry', 'dependency_status',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.dependent_areas'
        db.add_column(u'main_ciawfbentry', 'dependent_areas',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.diplomatic_representation_from_the_us'
        db.add_column(u'main_ciawfbentry', 'diplomatic_representation_from_the_us',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.diplomatic_representation_in_the_us'
        db.add_column(u'main_ciawfbentry', 'diplomatic_representation_in_the_us',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.disputes_international'
        db.add_column(u'main_ciawfbentry', 'disputes_international',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.distribution_of_family_income_gini_index'
        db.add_column(u'main_ciawfbentry', 'distribution_of_family_income_gini_index',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.drinking_water_source'
        db.add_column(u'main_ciawfbentry', 'drinking_water_source',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.economy_overview'
        db.add_column(u'main_ciawfbentry', 'economy_overview',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.education_expenditures'
        db.add_column(u'main_ciawfbentry', 'education_expenditures',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_consumption'
        db.add_column(u'main_ciawfbentry', 'electricity_consumption',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_exports'
        db.add_column(u'main_ciawfbentry', 'electricity_exports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_from_fossil_fuels'
        db.add_column(u'main_ciawfbentry', 'electricity_from_fossil_fuels',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_from_hydroelectric_plants'
        db.add_column(u'main_ciawfbentry', 'electricity_from_hydroelectric_plants',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_from_nuclear_fuels'
        db.add_column(u'main_ciawfbentry', 'electricity_from_nuclear_fuels',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_from_other_renewable_sources'
        db.add_column(u'main_ciawfbentry', 'electricity_from_other_renewable_sources',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_imports'
        db.add_column(u'main_ciawfbentry', 'electricity_imports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_installed_generating_capacity'
        db.add_column(u'main_ciawfbentry', 'electricity_installed_generating_capacity',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.electricity_production'
        db.add_column(u'main_ciawfbentry', 'electricity_production',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.elevation_extremes'
        db.add_column(u'main_ciawfbentry', 'elevation_extremes',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.environment_international_agreements'
        db.add_column(u'main_ciawfbentry', 'environment_international_agreements',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.ethnic_groups'
        db.add_column(u'main_ciawfbentry', 'ethnic_groups',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.exchange_rates'
        db.add_column(u'main_ciawfbentry', 'exchange_rates',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.executive_branch'
        db.add_column(u'main_ciawfbentry', 'executive_branch',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.exports'
        db.add_column(u'main_ciawfbentry', 'exports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.exports_commodities'
        db.add_column(u'main_ciawfbentry', 'exports_commodities',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.exports_partners'
        db.add_column(u'main_ciawfbentry', 'exports_partners',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.fiscal_year'
        db.add_column(u'main_ciawfbentry', 'fiscal_year',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.flag_description'
        db.add_column(u'main_ciawfbentry', 'flag_description',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.freshwater_withdrawal_domesticindustrialagricultural'
        db.add_column(u'main_ciawfbentry', 'freshwater_withdrawal_domesticindustrialagricultural',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.gdp_official_exchange_rate'
        db.add_column(u'main_ciawfbentry', 'gdp_official_exchange_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.gdp_purchasing_power_parity'
        db.add_column(u'main_ciawfbentry', 'gdp_purchasing_power_parity',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.gdp_composition_by_sector'
        db.add_column(u'main_ciawfbentry', 'gdp_composition_by_sector',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.gdp_per_capita_ppp'
        db.add_column(u'main_ciawfbentry', 'gdp_per_capita_ppp',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.gdp_real_growth_rate'
        db.add_column(u'main_ciawfbentry', 'gdp_real_growth_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.geographic_coordinates'
        db.add_column(u'main_ciawfbentry', 'geographic_coordinates',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.geography_note'
        db.add_column(u'main_ciawfbentry', 'geography_note',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.government_note'
        db.add_column(u'main_ciawfbentry', 'government_note',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.government_type'
        db.add_column(u'main_ciawfbentry', 'government_type',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.health_expenditures'
        db.add_column(u'main_ciawfbentry', 'health_expenditures',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.heliports'
        db.add_column(u'main_ciawfbentry', 'heliports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.hivaids_adult_prevalence_rate'
        db.add_column(u'main_ciawfbentry', 'hivaids_adult_prevalence_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.hivaids_deaths'
        db.add_column(u'main_ciawfbentry', 'hivaids_deaths',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.hivaids_people_living_with_hivaids'
        db.add_column(u'main_ciawfbentry', 'hivaids_people_living_with_hivaids',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.hospital_bed_density'
        db.add_column(u'main_ciawfbentry', 'hospital_bed_density',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.household_income_or_consumption_by_percentage_share'
        db.add_column(u'main_ciawfbentry', 'household_income_or_consumption_by_percentage_share',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.illicit_drugs'
        db.add_column(u'main_ciawfbentry', 'illicit_drugs',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.imports'
        db.add_column(u'main_ciawfbentry', 'imports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.imports_commodities'
        db.add_column(u'main_ciawfbentry', 'imports_commodities',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.imports_partners'
        db.add_column(u'main_ciawfbentry', 'imports_partners',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.independence'
        db.add_column(u'main_ciawfbentry', 'independence',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.industrial_production_growth_rate'
        db.add_column(u'main_ciawfbentry', 'industrial_production_growth_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.industries'
        db.add_column(u'main_ciawfbentry', 'industries',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.infant_mortality_rate'
        db.add_column(u'main_ciawfbentry', 'infant_mortality_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.inflation_rate_consumer_prices'
        db.add_column(u'main_ciawfbentry', 'inflation_rate_consumer_prices',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.international_law_organization_participation'
        db.add_column(u'main_ciawfbentry', 'international_law_organization_participation',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.international_organization_participation'
        db.add_column(u'main_ciawfbentry', 'international_organization_participation',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.internet_country_code'
        db.add_column(u'main_ciawfbentry', 'internet_country_code',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.internet_hosts'
        db.add_column(u'main_ciawfbentry', 'internet_hosts',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.internet_users'
        db.add_column(u'main_ciawfbentry', 'internet_users',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.investment_gross_fixed'
        db.add_column(u'main_ciawfbentry', 'investment_gross_fixed',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.irrigated_land'
        db.add_column(u'main_ciawfbentry', 'irrigated_land',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.judicial_branch'
        db.add_column(u'main_ciawfbentry', 'judicial_branch',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.labor_force'
        db.add_column(u'main_ciawfbentry', 'labor_force',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.labor_force_by_occupation'
        db.add_column(u'main_ciawfbentry', 'labor_force_by_occupation',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.land_boundaries'
        db.add_column(u'main_ciawfbentry', 'land_boundaries',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.land_use'
        db.add_column(u'main_ciawfbentry', 'land_use',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.languages'
        db.add_column(u'main_ciawfbentry', 'languages',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.legal_system'
        db.add_column(u'main_ciawfbentry', 'legal_system',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.legislative_branch'
        db.add_column(u'main_ciawfbentry', 'legislative_branch',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.life_expectancy_at_birth'
        db.add_column(u'main_ciawfbentry', 'life_expectancy_at_birth',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.literacy'
        db.add_column(u'main_ciawfbentry', 'literacy',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.major_cities_population'
        db.add_column(u'main_ciawfbentry', 'major_cities_population',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.major_infectious_diseases'
        db.add_column(u'main_ciawfbentry', 'major_infectious_diseases',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.manpower_available_for_military_service'
        db.add_column(u'main_ciawfbentry', 'manpower_available_for_military_service',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.manpower_fit_for_military_service'
        db.add_column(u'main_ciawfbentry', 'manpower_fit_for_military_service',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.manpower_reaching_militarily_significant_age_annually'
        db.add_column(u'main_ciawfbentry', 'manpower_reaching_militarily_significant_age_annually',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.map_references'
        db.add_column(u'main_ciawfbentry', 'map_references',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.maritime_claims'
        db.add_column(u'main_ciawfbentry', 'maritime_claims',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.market_value_of_publicly_traded_shares'
        db.add_column(u'main_ciawfbentry', 'market_value_of_publicly_traded_shares',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.maternal_mortality_rate'
        db.add_column(u'main_ciawfbentry', 'maternal_mortality_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.median_age'
        db.add_column(u'main_ciawfbentry', 'median_age',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.merchant_marine'
        db.add_column(u'main_ciawfbentry', 'merchant_marine',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.military_note'
        db.add_column(u'main_ciawfbentry', 'military_note',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.military_branches'
        db.add_column(u'main_ciawfbentry', 'military_branches',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.military_expenditures'
        db.add_column(u'main_ciawfbentry', 'military_expenditures',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.military_service_age_and_obligation'
        db.add_column(u'main_ciawfbentry', 'military_service_age_and_obligation',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.national_anthem'
        db.add_column(u'main_ciawfbentry', 'national_anthem',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.national_holiday'
        db.add_column(u'main_ciawfbentry', 'national_holiday',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.national_symbols'
        db.add_column(u'main_ciawfbentry', 'national_symbols',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.nationality'
        db.add_column(u'main_ciawfbentry', 'nationality',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.natural_gas_consumption'
        db.add_column(u'main_ciawfbentry', 'natural_gas_consumption',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.natural_gas_exports'
        db.add_column(u'main_ciawfbentry', 'natural_gas_exports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.natural_gas_imports'
        db.add_column(u'main_ciawfbentry', 'natural_gas_imports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.natural_gas_production'
        db.add_column(u'main_ciawfbentry', 'natural_gas_production',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.natural_gas_proved_reserves'
        db.add_column(u'main_ciawfbentry', 'natural_gas_proved_reserves',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.natural_resources'
        db.add_column(u'main_ciawfbentry', 'natural_resources',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.net_migration_rate'
        db.add_column(u'main_ciawfbentry', 'net_migration_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.obesity_adult_prevalence_rate'
        db.add_column(u'main_ciawfbentry', 'obesity_adult_prevalence_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.people_note'
        db.add_column(u'main_ciawfbentry', 'people_note',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.physicians_density'
        db.add_column(u'main_ciawfbentry', 'physicians_density',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.pipelines'
        db.add_column(u'main_ciawfbentry', 'pipelines',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.political_parties_and_leaders'
        db.add_column(u'main_ciawfbentry', 'political_parties_and_leaders',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.political_pressure_groups_and_leaders'
        db.add_column(u'main_ciawfbentry', 'political_pressure_groups_and_leaders',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.population'
        db.add_column(u'main_ciawfbentry', 'population',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.population_below_poverty_line'
        db.add_column(u'main_ciawfbentry', 'population_below_poverty_line',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.population_growth_rate'
        db.add_column(u'main_ciawfbentry', 'population_growth_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.ports_and_terminals'
        db.add_column(u'main_ciawfbentry', 'ports_and_terminals',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.public_debt'
        db.add_column(u'main_ciawfbentry', 'public_debt',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.railways'
        db.add_column(u'main_ciawfbentry', 'railways',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.refined_petroleum_products_consumption'
        db.add_column(u'main_ciawfbentry', 'refined_petroleum_products_consumption',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.refined_petroleum_products_exports'
        db.add_column(u'main_ciawfbentry', 'refined_petroleum_products_exports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.refined_petroleum_products_imports'
        db.add_column(u'main_ciawfbentry', 'refined_petroleum_products_imports',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.refined_petroleum_products_production'
        db.add_column(u'main_ciawfbentry', 'refined_petroleum_products_production',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.refugees_and_internally_displaced_persons'
        db.add_column(u'main_ciawfbentry', 'refugees_and_internally_displaced_persons',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.religions'
        db.add_column(u'main_ciawfbentry', 'religions',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.reserves_of_foreign_exchange_and_gold'
        db.add_column(u'main_ciawfbentry', 'reserves_of_foreign_exchange_and_gold',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.roadways'
        db.add_column(u'main_ciawfbentry', 'roadways',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.sanitation_facility_access'
        db.add_column(u'main_ciawfbentry', 'sanitation_facility_access',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.school_life_expectancy_primary_to_tertiary_education'
        db.add_column(u'main_ciawfbentry', 'school_life_expectancy_primary_to_tertiary_education',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.sex_ratio'
        db.add_column(u'main_ciawfbentry', 'sex_ratio',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.stock_of_broad_money'
        db.add_column(u'main_ciawfbentry', 'stock_of_broad_money',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.stock_of_direct_foreign_investment_abroad'
        db.add_column(u'main_ciawfbentry', 'stock_of_direct_foreign_investment_abroad',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.stock_of_direct_foreign_investment_at_home'
        db.add_column(u'main_ciawfbentry', 'stock_of_direct_foreign_investment_at_home',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.stock_of_domestic_credit'
        db.add_column(u'main_ciawfbentry', 'stock_of_domestic_credit',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.stock_of_narrow_money'
        db.add_column(u'main_ciawfbentry', 'stock_of_narrow_money',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.suffrage'
        db.add_column(u'main_ciawfbentry', 'suffrage',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.taxes_and_other_revenues'
        db.add_column(u'main_ciawfbentry', 'taxes_and_other_revenues',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.telephone_system'
        db.add_column(u'main_ciawfbentry', 'telephone_system',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.telephones_main_lines_in_use'
        db.add_column(u'main_ciawfbentry', 'telephones_main_lines_in_use',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.telephones_mobile_cellular'
        db.add_column(u'main_ciawfbentry', 'telephones_mobile_cellular',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.total_fertility_rate'
        db.add_column(u'main_ciawfbentry', 'total_fertility_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.total_renewable_water_resources'
        db.add_column(u'main_ciawfbentry', 'total_renewable_water_resources',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.trafficking_in_persons'
        db.add_column(u'main_ciawfbentry', 'trafficking_in_persons',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.transportation_note'
        db.add_column(u'main_ciawfbentry', 'transportation_note',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.unemployment_rate'
        db.add_column(u'main_ciawfbentry', 'unemployment_rate',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.unemployment_youth_ages_15_24'
        db.add_column(u'main_ciawfbentry', 'unemployment_youth_ages_15_24',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.urbanization'
        db.add_column(u'main_ciawfbentry', 'urbanization',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.waterways'
        db.add_column(u'main_ciawfbentry', 'waterways',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'CIAWFBEntry.background'
        db.alter_column(u'main_ciawfbentry', 'background', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CIAWFBEntry.terrain'
        db.alter_column(u'main_ciawfbentry', 'terrain', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CIAWFBEntry.climate'
        db.alter_column(u'main_ciawfbentry', 'climate', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CIAWFBEntry.natural_hazards'
        db.alter_column(u'main_ciawfbentry', 'natural_hazards', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'CIAWFBEntry.environment_current_issues'
        db.alter_column(u'main_ciawfbentry', 'environment_current_issues', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):
        # Adding field 'CIAWFBEntry.total_population_life_expectancy_at_birth'
        db.add_column(u'main_ciawfbentry', 'total_population_life_expectancy_at_birth',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.annual_freshwater_withdrawal_cu_km'
        db.add_column(u'main_ciawfbentry', 'annual_freshwater_withdrawal_cu_km',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.GDP_real_growth_rate_percentage'
        db.add_column(u'main_ciawfbentry', 'GDP_real_growth_rate_percentage',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.HIVAIDS_adult_prevalance_rate_percent'
        db.add_column(u'main_ciawfbentry', 'HIVAIDS_adult_prevalance_rate_percent',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.public_debt_as_percentage_of_GDP'
        db.add_column(u'main_ciawfbentry', 'public_debt_as_percentage_of_GDP',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.annual_renewable_water_resources_cu_km'
        db.add_column(u'main_ciawfbentry', 'annual_renewable_water_resources_cu_km',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.economic_narrative'
        db.add_column(u'main_ciawfbentry', 'economic_narrative',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.country_name_long'
        db.add_column(u'main_ciawfbentry', 'country_name_long',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CIAWFBEntry.consumer_prices_inflation_rate_percent'
        db.add_column(u'main_ciawfbentry', 'consumer_prices_inflation_rate_percent',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Deleting field 'CIAWFBEntry.administrative_divisions'
        db.delete_column(u'main_ciawfbentry', 'administrative_divisions')

        # Deleting field 'CIAWFBEntry.age_structure'
        db.delete_column(u'main_ciawfbentry', 'age_structure')

        # Deleting field 'CIAWFBEntry.airports'
        db.delete_column(u'main_ciawfbentry', 'airports')

        # Deleting field 'CIAWFBEntry.airports_with_paved_runways'
        db.delete_column(u'main_ciawfbentry', 'airports_with_paved_runways')

        # Deleting field 'CIAWFBEntry.airports_with_unpaved_runways'
        db.delete_column(u'main_ciawfbentry', 'airports_with_unpaved_runways')

        # Deleting field 'CIAWFBEntry.area'
        db.delete_column(u'main_ciawfbentry', 'area')

        # Deleting field 'CIAWFBEntry.area_comparative'
        db.delete_column(u'main_ciawfbentry', 'area_comparative')

        # Deleting field 'CIAWFBEntry.birth_rate'
        db.delete_column(u'main_ciawfbentry', 'birth_rate')

        # Deleting field 'CIAWFBEntry.broadcast_media'
        db.delete_column(u'main_ciawfbentry', 'broadcast_media')

        # Deleting field 'CIAWFBEntry.budget'
        db.delete_column(u'main_ciawfbentry', 'budget')

        # Deleting field 'CIAWFBEntry.budget_surplus_or_deficit'
        db.delete_column(u'main_ciawfbentry', 'budget_surplus_or_deficit')

        # Deleting field 'CIAWFBEntry.capital'
        db.delete_column(u'main_ciawfbentry', 'capital')

        # Deleting field 'CIAWFBEntry.carbon_dioxide_emissions_from_consumption_of_energy'
        db.delete_column(u'main_ciawfbentry', 'carbon_dioxide_emissions_from_consumption_of_energy')

        # Deleting field 'CIAWFBEntry.central_bank_discount_rate'
        db.delete_column(u'main_ciawfbentry', 'central_bank_discount_rate')

        # Deleting field 'CIAWFBEntry.children_under_the_age_of_5_years_underweight'
        db.delete_column(u'main_ciawfbentry', 'children_under_the_age_of_5_years_underweight')

        # Deleting field 'CIAWFBEntry.coastline'
        db.delete_column(u'main_ciawfbentry', 'coastline')

        # Deleting field 'CIAWFBEntry.commercial_bank_prime_lending_rate'
        db.delete_column(u'main_ciawfbentry', 'commercial_bank_prime_lending_rate')

        # Deleting field 'CIAWFBEntry.communications_note'
        db.delete_column(u'main_ciawfbentry', 'communications_note')

        # Deleting field 'CIAWFBEntry.constitution'
        db.delete_column(u'main_ciawfbentry', 'constitution')

        # Deleting field 'CIAWFBEntry.country_name'
        db.delete_column(u'main_ciawfbentry', 'country_name')

        # Deleting field 'CIAWFBEntry.crude_oil_exports'
        db.delete_column(u'main_ciawfbentry', 'crude_oil_exports')

        # Deleting field 'CIAWFBEntry.crude_oil_imports'
        db.delete_column(u'main_ciawfbentry', 'crude_oil_imports')

        # Deleting field 'CIAWFBEntry.crude_oil_production'
        db.delete_column(u'main_ciawfbentry', 'crude_oil_production')

        # Deleting field 'CIAWFBEntry.crude_oil_proved_reserves'
        db.delete_column(u'main_ciawfbentry', 'crude_oil_proved_reserves')

        # Deleting field 'CIAWFBEntry.current_account_balance'
        db.delete_column(u'main_ciawfbentry', 'current_account_balance')

        # Deleting field 'CIAWFBEntry.death_rate'
        db.delete_column(u'main_ciawfbentry', 'death_rate')

        # Deleting field 'CIAWFBEntry.debt_external'
        db.delete_column(u'main_ciawfbentry', 'debt_external')

        # Deleting field 'CIAWFBEntry.demographic_profile'
        db.delete_column(u'main_ciawfbentry', 'demographic_profile')

        # Deleting field 'CIAWFBEntry.dependency_status'
        db.delete_column(u'main_ciawfbentry', 'dependency_status')

        # Deleting field 'CIAWFBEntry.dependent_areas'
        db.delete_column(u'main_ciawfbentry', 'dependent_areas')

        # Deleting field 'CIAWFBEntry.diplomatic_representation_from_the_us'
        db.delete_column(u'main_ciawfbentry', 'diplomatic_representation_from_the_us')

        # Deleting field 'CIAWFBEntry.diplomatic_representation_in_the_us'
        db.delete_column(u'main_ciawfbentry', 'diplomatic_representation_in_the_us')

        # Deleting field 'CIAWFBEntry.disputes_international'
        db.delete_column(u'main_ciawfbentry', 'disputes_international')

        # Deleting field 'CIAWFBEntry.distribution_of_family_income_gini_index'
        db.delete_column(u'main_ciawfbentry', 'distribution_of_family_income_gini_index')

        # Deleting field 'CIAWFBEntry.drinking_water_source'
        db.delete_column(u'main_ciawfbentry', 'drinking_water_source')

        # Deleting field 'CIAWFBEntry.economy_overview'
        db.delete_column(u'main_ciawfbentry', 'economy_overview')

        # Deleting field 'CIAWFBEntry.education_expenditures'
        db.delete_column(u'main_ciawfbentry', 'education_expenditures')

        # Deleting field 'CIAWFBEntry.electricity_consumption'
        db.delete_column(u'main_ciawfbentry', 'electricity_consumption')

        # Deleting field 'CIAWFBEntry.electricity_exports'
        db.delete_column(u'main_ciawfbentry', 'electricity_exports')

        # Deleting field 'CIAWFBEntry.electricity_from_fossil_fuels'
        db.delete_column(u'main_ciawfbentry', 'electricity_from_fossil_fuels')

        # Deleting field 'CIAWFBEntry.electricity_from_hydroelectric_plants'
        db.delete_column(u'main_ciawfbentry', 'electricity_from_hydroelectric_plants')

        # Deleting field 'CIAWFBEntry.electricity_from_nuclear_fuels'
        db.delete_column(u'main_ciawfbentry', 'electricity_from_nuclear_fuels')

        # Deleting field 'CIAWFBEntry.electricity_from_other_renewable_sources'
        db.delete_column(u'main_ciawfbentry', 'electricity_from_other_renewable_sources')

        # Deleting field 'CIAWFBEntry.electricity_imports'
        db.delete_column(u'main_ciawfbentry', 'electricity_imports')

        # Deleting field 'CIAWFBEntry.electricity_installed_generating_capacity'
        db.delete_column(u'main_ciawfbentry', 'electricity_installed_generating_capacity')

        # Deleting field 'CIAWFBEntry.electricity_production'
        db.delete_column(u'main_ciawfbentry', 'electricity_production')

        # Deleting field 'CIAWFBEntry.elevation_extremes'
        db.delete_column(u'main_ciawfbentry', 'elevation_extremes')

        # Deleting field 'CIAWFBEntry.environment_international_agreements'
        db.delete_column(u'main_ciawfbentry', 'environment_international_agreements')

        # Deleting field 'CIAWFBEntry.ethnic_groups'
        db.delete_column(u'main_ciawfbentry', 'ethnic_groups')

        # Deleting field 'CIAWFBEntry.exchange_rates'
        db.delete_column(u'main_ciawfbentry', 'exchange_rates')

        # Deleting field 'CIAWFBEntry.executive_branch'
        db.delete_column(u'main_ciawfbentry', 'executive_branch')

        # Deleting field 'CIAWFBEntry.exports'
        db.delete_column(u'main_ciawfbentry', 'exports')

        # Deleting field 'CIAWFBEntry.exports_commodities'
        db.delete_column(u'main_ciawfbentry', 'exports_commodities')

        # Deleting field 'CIAWFBEntry.exports_partners'
        db.delete_column(u'main_ciawfbentry', 'exports_partners')

        # Deleting field 'CIAWFBEntry.fiscal_year'
        db.delete_column(u'main_ciawfbentry', 'fiscal_year')

        # Deleting field 'CIAWFBEntry.flag_description'
        db.delete_column(u'main_ciawfbentry', 'flag_description')

        # Deleting field 'CIAWFBEntry.freshwater_withdrawal_domesticindustrialagricultural'
        db.delete_column(u'main_ciawfbentry', 'freshwater_withdrawal_domesticindustrialagricultural')

        # Deleting field 'CIAWFBEntry.gdp_official_exchange_rate'
        db.delete_column(u'main_ciawfbentry', 'gdp_official_exchange_rate')

        # Deleting field 'CIAWFBEntry.gdp_purchasing_power_parity'
        db.delete_column(u'main_ciawfbentry', 'gdp_purchasing_power_parity')

        # Deleting field 'CIAWFBEntry.gdp_composition_by_sector'
        db.delete_column(u'main_ciawfbentry', 'gdp_composition_by_sector')

        # Deleting field 'CIAWFBEntry.gdp_per_capita_ppp'
        db.delete_column(u'main_ciawfbentry', 'gdp_per_capita_ppp')

        # Deleting field 'CIAWFBEntry.gdp_real_growth_rate'
        db.delete_column(u'main_ciawfbentry', 'gdp_real_growth_rate')

        # Deleting field 'CIAWFBEntry.geographic_coordinates'
        db.delete_column(u'main_ciawfbentry', 'geographic_coordinates')

        # Deleting field 'CIAWFBEntry.geography_note'
        db.delete_column(u'main_ciawfbentry', 'geography_note')

        # Deleting field 'CIAWFBEntry.government_note'
        db.delete_column(u'main_ciawfbentry', 'government_note')

        # Deleting field 'CIAWFBEntry.government_type'
        db.delete_column(u'main_ciawfbentry', 'government_type')

        # Deleting field 'CIAWFBEntry.health_expenditures'
        db.delete_column(u'main_ciawfbentry', 'health_expenditures')

        # Deleting field 'CIAWFBEntry.heliports'
        db.delete_column(u'main_ciawfbentry', 'heliports')

        # Deleting field 'CIAWFBEntry.hivaids_adult_prevalence_rate'
        db.delete_column(u'main_ciawfbentry', 'hivaids_adult_prevalence_rate')

        # Deleting field 'CIAWFBEntry.hivaids_deaths'
        db.delete_column(u'main_ciawfbentry', 'hivaids_deaths')

        # Deleting field 'CIAWFBEntry.hivaids_people_living_with_hivaids'
        db.delete_column(u'main_ciawfbentry', 'hivaids_people_living_with_hivaids')

        # Deleting field 'CIAWFBEntry.hospital_bed_density'
        db.delete_column(u'main_ciawfbentry', 'hospital_bed_density')

        # Deleting field 'CIAWFBEntry.household_income_or_consumption_by_percentage_share'
        db.delete_column(u'main_ciawfbentry', 'household_income_or_consumption_by_percentage_share')

        # Deleting field 'CIAWFBEntry.illicit_drugs'
        db.delete_column(u'main_ciawfbentry', 'illicit_drugs')

        # Deleting field 'CIAWFBEntry.imports'
        db.delete_column(u'main_ciawfbentry', 'imports')

        # Deleting field 'CIAWFBEntry.imports_commodities'
        db.delete_column(u'main_ciawfbentry', 'imports_commodities')

        # Deleting field 'CIAWFBEntry.imports_partners'
        db.delete_column(u'main_ciawfbentry', 'imports_partners')

        # Deleting field 'CIAWFBEntry.independence'
        db.delete_column(u'main_ciawfbentry', 'independence')

        # Deleting field 'CIAWFBEntry.industrial_production_growth_rate'
        db.delete_column(u'main_ciawfbentry', 'industrial_production_growth_rate')

        # Deleting field 'CIAWFBEntry.industries'
        db.delete_column(u'main_ciawfbentry', 'industries')

        # Deleting field 'CIAWFBEntry.infant_mortality_rate'
        db.delete_column(u'main_ciawfbentry', 'infant_mortality_rate')

        # Deleting field 'CIAWFBEntry.inflation_rate_consumer_prices'
        db.delete_column(u'main_ciawfbentry', 'inflation_rate_consumer_prices')

        # Deleting field 'CIAWFBEntry.international_law_organization_participation'
        db.delete_column(u'main_ciawfbentry', 'international_law_organization_participation')

        # Deleting field 'CIAWFBEntry.international_organization_participation'
        db.delete_column(u'main_ciawfbentry', 'international_organization_participation')

        # Deleting field 'CIAWFBEntry.internet_country_code'
        db.delete_column(u'main_ciawfbentry', 'internet_country_code')

        # Deleting field 'CIAWFBEntry.internet_hosts'
        db.delete_column(u'main_ciawfbentry', 'internet_hosts')

        # Deleting field 'CIAWFBEntry.internet_users'
        db.delete_column(u'main_ciawfbentry', 'internet_users')

        # Deleting field 'CIAWFBEntry.investment_gross_fixed'
        db.delete_column(u'main_ciawfbentry', 'investment_gross_fixed')

        # Deleting field 'CIAWFBEntry.irrigated_land'
        db.delete_column(u'main_ciawfbentry', 'irrigated_land')

        # Deleting field 'CIAWFBEntry.judicial_branch'
        db.delete_column(u'main_ciawfbentry', 'judicial_branch')

        # Deleting field 'CIAWFBEntry.labor_force'
        db.delete_column(u'main_ciawfbentry', 'labor_force')

        # Deleting field 'CIAWFBEntry.labor_force_by_occupation'
        db.delete_column(u'main_ciawfbentry', 'labor_force_by_occupation')

        # Deleting field 'CIAWFBEntry.land_boundaries'
        db.delete_column(u'main_ciawfbentry', 'land_boundaries')

        # Deleting field 'CIAWFBEntry.land_use'
        db.delete_column(u'main_ciawfbentry', 'land_use')

        # Deleting field 'CIAWFBEntry.languages'
        db.delete_column(u'main_ciawfbentry', 'languages')

        # Deleting field 'CIAWFBEntry.legal_system'
        db.delete_column(u'main_ciawfbentry', 'legal_system')

        # Deleting field 'CIAWFBEntry.legislative_branch'
        db.delete_column(u'main_ciawfbentry', 'legislative_branch')

        # Deleting field 'CIAWFBEntry.life_expectancy_at_birth'
        db.delete_column(u'main_ciawfbentry', 'life_expectancy_at_birth')

        # Deleting field 'CIAWFBEntry.literacy'
        db.delete_column(u'main_ciawfbentry', 'literacy')

        # Deleting field 'CIAWFBEntry.major_cities_population'
        db.delete_column(u'main_ciawfbentry', 'major_cities_population')

        # Deleting field 'CIAWFBEntry.major_infectious_diseases'
        db.delete_column(u'main_ciawfbentry', 'major_infectious_diseases')

        # Deleting field 'CIAWFBEntry.manpower_available_for_military_service'
        db.delete_column(u'main_ciawfbentry', 'manpower_available_for_military_service')

        # Deleting field 'CIAWFBEntry.manpower_fit_for_military_service'
        db.delete_column(u'main_ciawfbentry', 'manpower_fit_for_military_service')

        # Deleting field 'CIAWFBEntry.manpower_reaching_militarily_significant_age_annually'
        db.delete_column(u'main_ciawfbentry', 'manpower_reaching_militarily_significant_age_annually')

        # Deleting field 'CIAWFBEntry.map_references'
        db.delete_column(u'main_ciawfbentry', 'map_references')

        # Deleting field 'CIAWFBEntry.maritime_claims'
        db.delete_column(u'main_ciawfbentry', 'maritime_claims')

        # Deleting field 'CIAWFBEntry.market_value_of_publicly_traded_shares'
        db.delete_column(u'main_ciawfbentry', 'market_value_of_publicly_traded_shares')

        # Deleting field 'CIAWFBEntry.maternal_mortality_rate'
        db.delete_column(u'main_ciawfbentry', 'maternal_mortality_rate')

        # Deleting field 'CIAWFBEntry.median_age'
        db.delete_column(u'main_ciawfbentry', 'median_age')

        # Deleting field 'CIAWFBEntry.merchant_marine'
        db.delete_column(u'main_ciawfbentry', 'merchant_marine')

        # Deleting field 'CIAWFBEntry.military_note'
        db.delete_column(u'main_ciawfbentry', 'military_note')

        # Deleting field 'CIAWFBEntry.military_branches'
        db.delete_column(u'main_ciawfbentry', 'military_branches')

        # Deleting field 'CIAWFBEntry.military_expenditures'
        db.delete_column(u'main_ciawfbentry', 'military_expenditures')

        # Deleting field 'CIAWFBEntry.military_service_age_and_obligation'
        db.delete_column(u'main_ciawfbentry', 'military_service_age_and_obligation')

        # Deleting field 'CIAWFBEntry.national_anthem'
        db.delete_column(u'main_ciawfbentry', 'national_anthem')

        # Deleting field 'CIAWFBEntry.national_holiday'
        db.delete_column(u'main_ciawfbentry', 'national_holiday')

        # Deleting field 'CIAWFBEntry.national_symbols'
        db.delete_column(u'main_ciawfbentry', 'national_symbols')

        # Deleting field 'CIAWFBEntry.nationality'
        db.delete_column(u'main_ciawfbentry', 'nationality')

        # Deleting field 'CIAWFBEntry.natural_gas_consumption'
        db.delete_column(u'main_ciawfbentry', 'natural_gas_consumption')

        # Deleting field 'CIAWFBEntry.natural_gas_exports'
        db.delete_column(u'main_ciawfbentry', 'natural_gas_exports')

        # Deleting field 'CIAWFBEntry.natural_gas_imports'
        db.delete_column(u'main_ciawfbentry', 'natural_gas_imports')

        # Deleting field 'CIAWFBEntry.natural_gas_production'
        db.delete_column(u'main_ciawfbentry', 'natural_gas_production')

        # Deleting field 'CIAWFBEntry.natural_gas_proved_reserves'
        db.delete_column(u'main_ciawfbentry', 'natural_gas_proved_reserves')

        # Deleting field 'CIAWFBEntry.natural_resources'
        db.delete_column(u'main_ciawfbentry', 'natural_resources')

        # Deleting field 'CIAWFBEntry.net_migration_rate'
        db.delete_column(u'main_ciawfbentry', 'net_migration_rate')

        # Deleting field 'CIAWFBEntry.obesity_adult_prevalence_rate'
        db.delete_column(u'main_ciawfbentry', 'obesity_adult_prevalence_rate')

        # Deleting field 'CIAWFBEntry.people_note'
        db.delete_column(u'main_ciawfbentry', 'people_note')

        # Deleting field 'CIAWFBEntry.physicians_density'
        db.delete_column(u'main_ciawfbentry', 'physicians_density')

        # Deleting field 'CIAWFBEntry.pipelines'
        db.delete_column(u'main_ciawfbentry', 'pipelines')

        # Deleting field 'CIAWFBEntry.political_parties_and_leaders'
        db.delete_column(u'main_ciawfbentry', 'political_parties_and_leaders')

        # Deleting field 'CIAWFBEntry.political_pressure_groups_and_leaders'
        db.delete_column(u'main_ciawfbentry', 'political_pressure_groups_and_leaders')

        # Deleting field 'CIAWFBEntry.population'
        db.delete_column(u'main_ciawfbentry', 'population')

        # Deleting field 'CIAWFBEntry.population_below_poverty_line'
        db.delete_column(u'main_ciawfbentry', 'population_below_poverty_line')

        # Deleting field 'CIAWFBEntry.population_growth_rate'
        db.delete_column(u'main_ciawfbentry', 'population_growth_rate')

        # Deleting field 'CIAWFBEntry.ports_and_terminals'
        db.delete_column(u'main_ciawfbentry', 'ports_and_terminals')

        # Deleting field 'CIAWFBEntry.public_debt'
        db.delete_column(u'main_ciawfbentry', 'public_debt')

        # Deleting field 'CIAWFBEntry.railways'
        db.delete_column(u'main_ciawfbentry', 'railways')

        # Deleting field 'CIAWFBEntry.refined_petroleum_products_consumption'
        db.delete_column(u'main_ciawfbentry', 'refined_petroleum_products_consumption')

        # Deleting field 'CIAWFBEntry.refined_petroleum_products_exports'
        db.delete_column(u'main_ciawfbentry', 'refined_petroleum_products_exports')

        # Deleting field 'CIAWFBEntry.refined_petroleum_products_imports'
        db.delete_column(u'main_ciawfbentry', 'refined_petroleum_products_imports')

        # Deleting field 'CIAWFBEntry.refined_petroleum_products_production'
        db.delete_column(u'main_ciawfbentry', 'refined_petroleum_products_production')

        # Deleting field 'CIAWFBEntry.refugees_and_internally_displaced_persons'
        db.delete_column(u'main_ciawfbentry', 'refugees_and_internally_displaced_persons')

        # Deleting field 'CIAWFBEntry.religions'
        db.delete_column(u'main_ciawfbentry', 'religions')

        # Deleting field 'CIAWFBEntry.reserves_of_foreign_exchange_and_gold'
        db.delete_column(u'main_ciawfbentry', 'reserves_of_foreign_exchange_and_gold')

        # Deleting field 'CIAWFBEntry.roadways'
        db.delete_column(u'main_ciawfbentry', 'roadways')

        # Deleting field 'CIAWFBEntry.sanitation_facility_access'
        db.delete_column(u'main_ciawfbentry', 'sanitation_facility_access')

        # Deleting field 'CIAWFBEntry.school_life_expectancy_primary_to_tertiary_education'
        db.delete_column(u'main_ciawfbentry', 'school_life_expectancy_primary_to_tertiary_education')

        # Deleting field 'CIAWFBEntry.sex_ratio'
        db.delete_column(u'main_ciawfbentry', 'sex_ratio')

        # Deleting field 'CIAWFBEntry.stock_of_broad_money'
        db.delete_column(u'main_ciawfbentry', 'stock_of_broad_money')

        # Deleting field 'CIAWFBEntry.stock_of_direct_foreign_investment_abroad'
        db.delete_column(u'main_ciawfbentry', 'stock_of_direct_foreign_investment_abroad')

        # Deleting field 'CIAWFBEntry.stock_of_direct_foreign_investment_at_home'
        db.delete_column(u'main_ciawfbentry', 'stock_of_direct_foreign_investment_at_home')

        # Deleting field 'CIAWFBEntry.stock_of_domestic_credit'
        db.delete_column(u'main_ciawfbentry', 'stock_of_domestic_credit')

        # Deleting field 'CIAWFBEntry.stock_of_narrow_money'
        db.delete_column(u'main_ciawfbentry', 'stock_of_narrow_money')

        # Deleting field 'CIAWFBEntry.suffrage'
        db.delete_column(u'main_ciawfbentry', 'suffrage')

        # Deleting field 'CIAWFBEntry.taxes_and_other_revenues'
        db.delete_column(u'main_ciawfbentry', 'taxes_and_other_revenues')

        # Deleting field 'CIAWFBEntry.telephone_system'
        db.delete_column(u'main_ciawfbentry', 'telephone_system')

        # Deleting field 'CIAWFBEntry.telephones_main_lines_in_use'
        db.delete_column(u'main_ciawfbentry', 'telephones_main_lines_in_use')

        # Deleting field 'CIAWFBEntry.telephones_mobile_cellular'
        db.delete_column(u'main_ciawfbentry', 'telephones_mobile_cellular')

        # Deleting field 'CIAWFBEntry.total_fertility_rate'
        db.delete_column(u'main_ciawfbentry', 'total_fertility_rate')

        # Deleting field 'CIAWFBEntry.total_renewable_water_resources'
        db.delete_column(u'main_ciawfbentry', 'total_renewable_water_resources')

        # Deleting field 'CIAWFBEntry.trafficking_in_persons'
        db.delete_column(u'main_ciawfbentry', 'trafficking_in_persons')

        # Deleting field 'CIAWFBEntry.transportation_note'
        db.delete_column(u'main_ciawfbentry', 'transportation_note')

        # Deleting field 'CIAWFBEntry.unemployment_rate'
        db.delete_column(u'main_ciawfbentry', 'unemployment_rate')

        # Deleting field 'CIAWFBEntry.unemployment_youth_ages_15_24'
        db.delete_column(u'main_ciawfbentry', 'unemployment_youth_ages_15_24')

        # Deleting field 'CIAWFBEntry.urbanization'
        db.delete_column(u'main_ciawfbentry', 'urbanization')

        # Deleting field 'CIAWFBEntry.waterways'
        db.delete_column(u'main_ciawfbentry', 'waterways')


        # Changing field 'CIAWFBEntry.background'
        db.alter_column(u'main_ciawfbentry', 'background', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CIAWFBEntry.terrain'
        db.alter_column(u'main_ciawfbentry', 'terrain', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CIAWFBEntry.climate'
        db.alter_column(u'main_ciawfbentry', 'climate', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CIAWFBEntry.natural_hazards'
        db.alter_column(u'main_ciawfbentry', 'natural_hazards', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CIAWFBEntry.environment_current_issues'
        db.alter_column(u'main_ciawfbentry', 'environment_current_issues', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'main.ciawfbentry': {
            'Meta': {'object_name': 'CIAWFBEntry'},
            'administrative_divisions': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'age_structure': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'agriculture_products': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'airports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'airports_with_paved_runways': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'airports_with_unpaved_runways': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'area_comparative': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'background': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'birth_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'broadcast_media': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'budget': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'budget_surplus_or_deficit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'carbon_dioxide_emissions_from_consumption_of_energy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'central_bank_discount_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'children_under_the_age_of_5_years_underweight': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'climate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'coastline': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'commercial_bank_prime_lending_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'communications_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'constitution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Country']"}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'crude_oil_exports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'crude_oil_imports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'crude_oil_production': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'crude_oil_proved_reserves': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'current_account_balance': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_entered': ('django.db.models.fields.DateField', [], {}),
            'death_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'debt_external': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'demographic_profile': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dependency_status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dependent_areas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'diplomatic_representation_from_the_us': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'diplomatic_representation_in_the_us': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'disputes_international': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'distribution_of_family_income_gini_index': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'drinking_water_source': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'economy_overview': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'education_expenditures': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_consumption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_exports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_from_fossil_fuels': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_from_hydroelectric_plants': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_from_nuclear_fuels': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_from_other_renewable_sources': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_imports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_installed_generating_capacity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'electricity_production': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'elevation_extremes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'environment_current_issues': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'environment_international_agreements': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ethnic_groups': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'exchange_rates': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'executive_branch': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'exports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'exports_commodities': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'exports_partners': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fiscal_year': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'flag_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'freshwater_withdrawal_domesticindustrialagricultural': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gdp_composition_by_sector': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gdp_official_exchange_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gdp_per_capita_ppp': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gdp_purchasing_power_parity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gdp_real_growth_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'geographic_coordinates': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'geography_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'government_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'government_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'health_expenditures': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'heliports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hivaids_adult_prevalence_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hivaids_deaths': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hivaids_people_living_with_hivaids': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hospital_bed_density': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'household_income_or_consumption_by_percentage_share': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illicit_drugs': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'imports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'imports_commodities': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'imports_partners': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'independence': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'industrial_production_growth_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'industries': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'infant_mortality_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'inflation_rate_consumer_prices': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'international_law_organization_participation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'international_organization_participation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'internet_country_code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'internet_hosts': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'internet_users': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'investment_gross_fixed': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'irrigated_land': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'judicial_branch': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'labor_force': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'labor_force_by_occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'land_boundaries': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'land_use': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'legal_system': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'legislative_branch': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'life_expectancy_at_birth': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'literacy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'major_cities_population': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'major_infectious_diseases': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'manpower_available_for_military_service': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'manpower_fit_for_military_service': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'manpower_reaching_militarily_significant_age_annually': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'map_references': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'maritime_claims': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'market_value_of_publicly_traded_shares': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'maternal_mortality_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'median_age': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'merchant_marine': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'military_branches': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'military_expenditures': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'military_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'military_service_age_and_obligation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'national_anthem': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'national_holiday': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'national_symbols': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_gas_consumption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_gas_exports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_gas_imports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_gas_production': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_gas_proved_reserves': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_hazards': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'natural_resources': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'net_migration_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'obesity_adult_prevalence_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'people_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'physicians_density': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pipelines': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'political_parties_and_leaders': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'political_pressure_groups_and_leaders': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'population_below_poverty_line': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'population_growth_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ports_and_terminals': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'public_debt': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'railways': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'refined_petroleum_products_consumption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'refined_petroleum_products_exports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'refined_petroleum_products_imports': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'refined_petroleum_products_production': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'refugees_and_internally_displaced_persons': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'religions': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reserves_of_foreign_exchange_and_gold': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'roadways': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sanitation_facility_access': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'school_life_expectancy_primary_to_tertiary_education': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sex_ratio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stock_of_broad_money': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stock_of_direct_foreign_investment_abroad': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stock_of_direct_foreign_investment_at_home': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stock_of_domestic_credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stock_of_narrow_money': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'suffrage': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'taxes_and_other_revenues': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telephone_system': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telephones_main_lines_in_use': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telephones_mobile_cellular': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'terrain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'total_fertility_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'total_renewable_water_resources': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'trafficking_in_persons': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'transportation_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'unemployment_rate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'unemployment_youth_ages_15_24': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'urbanization': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'waterways': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'main.country': {
            'CIAWFB_name_short': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']