import urllib2
import re

import bs4

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.utils import timezone

from main.models import Country, CIAWFBEntry

field_data_codes = {'administrative_divisions': '2051',
                    'age_structure': '2010',
                    'agriculture_products': '2052',
                    'airports': '2053',
                    'airports_with_paved_runways': '2030',
                    'airports_with_unpaved_runways': '2031',
                    'area': '2147',
                    'area_comparative': '2023',
                    'background': '2028',
                    'birth_rate': '2054',
                    'broadcast_media': '2213',
                    'budget': '2056',
                    'budget_surplus_or_deficit_': '2222',
                    'capital': '2057',
                    'carbon_dioxide_emissions_from_consumption_of_energy': '2254',
                    'central_bank_discount_rate': '2207',
                    'children_under_the_age_of_5_years_underweight': '2224',
                    'climate': '2059',
                    'coastline': '2060',
                    'commercial_bank_prime_lending_rate': '2208',
                    'communications_note': '2138',
                    'constitution': '2063',
                    'country_name': '2142',
                    'crude_oil_exports': '2242',
                    'crude_oil_imports': '2243',
                    'crude_oil_production': '2241',
                    'crude_oil_proved_reserves': '2244',
                    'current_account_balance': '2187',
                    'death_rate': '2066',
                    'debt_external': '2079',
                    'demographic_profile': '2257',
                    'dependency_status': '2006',
                    'dependent_areas': '2068',
                    'diplomatic_representation_from_the_us': '2007',
                    'diplomatic_representation_in_the_us': '2149',
                    'disputes_international': '2070',
                    'distribution_of_family_income_gini_index': '2172',
                    'drinking_water_source': '2216',
                    'economy_overview': '2116',
                    'education_expenditures': '2206',
                    'electricity_consumption': '2233',
                    'electricity_exports': '2234',
                    'electricity_from_fossil_fuels': '2237',
                    'electricity_from_hydroelectric_plants': '2238',
                    'electricity_from_nuclear_fuels': '2239',
                    'electricity_from_other_renewable_sources': '2240',
                    'electricity_imports': '2235',
                    'electricity_installed_generating_capacity': '2236',
                    'electricity_production': '2232',
                    'elevation_extremes': '2020',
                    'environment_current_issues': '2032',
                    'environment_international_agreements': '2033',
                    'ethnic_groups': '2075',
                    'exchange_rates': '2076',
                    'executive_branch': '2077',
                    'exports': '2078',
                    'exports_commodities': '2049',
                    'exports_partners': '2050',
                    'fiscal_year': '2080',
                    'flag_description': '2081',
                    'freshwater_withdrawal_domesticindustrialagricultural': '2202',
                    'gdp_official_exchange_rate': '2195',
                    'gdp_purchasing_power_parity': '2001',
                    'gdp_composition_by_sector': '2012',
                    'gdp_per_capita_ppp': '2004',
                    'gdp_real_growth_rate': '2003',
                    'geographic_coordinates': '2011',
                    'geography_note': '2113',
                    'government_note': '2140',
                    'government_type': '2128',
                    'health_expenditures': '2225',
                    'heliports': '2019',
                    'hivaids_adult_prevalence_rate': '2155',
                    'hivaids_deaths': '2157',
                    'hivaids_people_living_with_hivaids': '2156',
                    'hospital_bed_density': '2227',
                    'household_income_or_consumption_by_percentage_share': '2047',
                    'illicit_drugs': '2086',
                    'imports': '2087',
                    'imports_commodities': '2058',
                    'imports_partners': '2061',
                    'independence': '2088',
                    'industrial_production_growth_rate': '2089',
                    'industries': '2090',
                    'infant_mortality_rate': '2091',
                    'inflation_rate_consumer_prices': '2092',
                    'international_law_organization_participation': '2220',
                    'international_organization_participation': '2107',
                    'internet_country_code': '2154',
                    'internet_hosts': '2184',
                    'internet_users': '2153',
                    'investment_gross_fixed': '2185',
                    'irrigated_land': '2146',
                    'judicial_branch': '2094',
                    'labor_force': '2095',
                    'labor_force_by_occupation': '2048',
                    'land_boundaries': '2096',
                    'land_use': '2097',
                    'languages': '2098',
                    'legal_system': '2100',
                    'legislative_branch': '2101',
                    'life_expectancy_at_birth': '2102',
                    'literacy': '2103',
                    'location': '2144',
                    'major_cities_population': '2219',
                    'major_infectious_diseases': '2193',
                    'manpower_available_for_military_service': '2105',
                    'manpower_fit_for_military_service': '2025',
                    'manpower_reaching_militarily_significant_age_annually': '2026',
                    'map_references': '2145',
                    'maritime_claims': '2106',
                    'market_value_of_publicly_traded_shares': '2200',
                    'maternal_mortality_rate': '2223',
                    'median_age': '2177',
                    'merchant_marine': '2108',
                    'military_note': '2137',
                    'military_branches': '2055',
                    'military_expenditures': '2034',
                    'military_service_age_and_obligation': '2024',
                    'national_anthem': '2218',
                    'national_holiday': '2109',
                    'national_symbols': '2230',
                    'nationality': '2110',
                    'natural_gas_consumption': '2250',
                    'natural_gas_exports': '2251',
                    'natural_gas_imports': '2252',
                    'natural_gas_production': '2249',
                    'natural_gas_proved_reserves': '2253',
                    'natural_hazards': '2021',
                    'natural_resources': '2111',
                    'net_migration_rate': '2112',
                    'obesity_adult_prevalence_rate': '2228',
                    'people_note': '2022',
                    'physicians_density': '2226',
                    'pipelines': '2117',
                    'political_parties_and_leaders': '2118',
                    'political_pressure_groups_and_leaders': '2115',
                    'population': '2119',
                    'population_below_poverty_line': '2046',
                    'population_growth_rate': '2002',
                    'ports_and_terminals': '2120',
                    'public_debt': '2186',
                    'railways': '2121',
                    'refined_petroleum_products_consumption': '2246',
                    'refined_petroleum_products_exports': '2247',
                    'refined_petroleum_products_imports': '2248',
                    'refined_petroleum_products_production': '2245',
                    'refugees_and_internally_displaced_persons': '2194',
                    'religions': '2122',
                    'reserves_of_foreign_exchange_and_gold': '2188',
                    'roadways': '2085',
                    'sanitation_facility_access': '2217',
                    'school_life_expectancy_primary_to_tertiary_education': '2205',
                    'sex_ratio': '2018',
                    'stock_of_broad_money': '2215',
                    'stock_of_direct_foreign_investment_abroad': '2199',
                    'stock_of_direct_foreign_investment_at_home': '2198',
                    'stock_of_domestic_credit': '2211',
                    'stock_of_narrow_money': '2214',
                    'suffrage': '2123',
                    'taxes_and_other_revenues': '2221',
                    'telephone_system': '2124',
                    'telephones_main_lines_in_use': '2150',
                    'telephones_mobile_cellular': '2151',
                    'terrain': '2125',
                    'total_fertility_rate': '2127',
                    'total_renewable_water_resources': '2201',
                    'trafficking_in_persons': '2196',
                    'transportation_note': '2008',
                    'unemployment_rate': '2129',
                    'unemployment_youth_ages_15_24': '2229',
                    'urbanization': '2212',
                    'waterways': '2093'}


class Command(BaseCommand):
    help = 'Updates Country Data from CIA World Factbook'

    def handle(self, *args, **options):

        def extract_field_data(field_name, field_url):
            """ Note: Requires HTML5 Library: pip intall html5lib
            """
            country_attribute_list = {}

            rootURL = "https://www.cia.gov/library/publications/the-world-factbook/fields/"
            fullURL = rootURL + field_url + '.html'
            soup = bs4.BeautifulSoup(urllib2.urlopen(fullURL).read())
            tables = soup.find_all('table', width="638")
            for table in tables:
                try:
                    country = table.find('a', href=re.compile('geos')).text.strip()
                except AttributeError:
                    continue

                try:
                    field_value = table.find('td', class_="category_data").text.strip()
                except AttributeError:
                    continue
                country_attribute_list[country] = field_value
            return country_attribute_list

        def write_field_data_to_db(field_name, field_data):
            for country_name in field_data.keys():

                # get country if it exists; create it if it doesn't.
                country_slug = slugify(country_name)
                try:
                    country = Country.objects.get(url_name=country_slug)
                except Country.DoesNotExist:
                    country = Country(url_name=country_slug)
                    country.CIAWFB_name_short = country_name
                    country.save()

                # Get CIA WFB Entry if it exists; create it if it doesn't.
                try:
                    CIAWFB_object = CIAWFBEntry.objects.get(country__id=country.id)
                except CIAWFBEntry.DoesNotExist:
                    CIAWFB_object = CIAWFBEntry(country=country, date_entered=timezone.now())
                    CIAWFB_object.save()

                # Now update the field we've got for that CIAWFB entry
                db_name = slugify(field_name).replace('-', '_')
                setattr(CIAWFB_object, db_name, field_data[country_name])
                CIAWFB_object.save()

        for field_name in field_data_codes.keys():
            field_data = extract_field_data(field_name, field_data_codes[field_name])
            write_field_data_to_db(field_name, field_data)
            # next: https://docs.djangoproject.com/en/dev/intro/tutorial01/
