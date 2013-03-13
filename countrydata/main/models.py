from django.db import models


class Country(models.Model):
    def __unicode__(self):
        return self.CIAWFB_name_short
    # We use the CIA World Factbook "conventional short form" of the country name
    # as our canonical source for country names.
    CIAWFB_name_short = models.CharField(max_length=100)


class CIAWFBEntry(models.Model):
    def __unicode__(self):
        return "%s (%s)" % (self.country_name_long, self.date_entered)

    country = models.ForeignKey(Country)

    date_entered = models.DateField()
    country_url = models.URLField()

    country_name_long = models.CharField(max_length=200, blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    climate = models.TextField(blank=True, null=True)
    terrain = models.TextField(blank=True, null=True)
    annual_renewable_water_resources_cu_km = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    annual_freshwater_withdrawal_cu_km = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    natural_hazards = models.TextField(blank=True, null=True)
    environment_current_issues = models.TextField(blank=True, null=True)
    total_population_life_expectancy_at_birth = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    HIVAIDS_adult_prevalance_rate_percent = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    economic_narrative = models.TextField(blank=True, null=True)
    GDP_real_growth_rate_percentage = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    public_debt_as_percentage_of_GDP = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    consumer_prices_inflation_rate_percent = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
