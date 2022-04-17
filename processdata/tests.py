from django.test import TestCase 
from processdata.getdata import *  
import datetime


# Verify that we can access our vaccine data
class VaccineDataExistsTest(TestCase):  


    def test_vaccine_data_exists(self):

        vaccine_df = vaccinated_report()
        self.assertTrue(len(vaccine_df) > 0) 

# Verify that we are properly filtering our vaccine data
class ContinentsNotInVaccineDataTest(TestCase): 

    def test_continents_not_in_vaccine_data_test(self): 

        continents = ['Oceania','Europe','Africa','North America','South America','Asia'] 

        daily_covid_data = daily_report()

        for continent in continents: 

            self.assertTrue(continent not in set(daily_covid_data['Country_Region'])) 

# Verify that the fully vaccinated metrics makes sense
class FullyVaccinatedTest(TestCase): 

    def test_fully_vaccinated(self): 

        WOLRD_POPULATION = 8000000000 

        daily_covid_data = daily_report() 

        self.assertTrue(max(daily_covid_data['people_fully_vaccinated']) < WOLRD_POPULATION and max(daily_covid_data['people_fully_vaccinated']) > 0) 

# Check if our vaccine data has been updated within the past week,
# if not, then this is a possible sign that our data source 
# is no longer being updated
class VaccineDataUpdatedTest(TestCase): 

    def test_vaccine_data_being_updated(self): 

        vaccine_df = vaccinated_report()  
        vaccine_df['date'] = pd.to_datetime(vaccine_df['date'])

        date_last_updated = max(vaccine_df['date'])  

        diff_in_time = datetime.datetime.today() - date_last_updated

        self.assertTrue(diff_in_time.days <= 7)

