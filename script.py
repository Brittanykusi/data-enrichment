import pandas as pd

## load in datasets ##
discharges = pd.read_csv('/Users/brittanykusi-gyabaah/Desktop/GitHub/data-enrichment/data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
discharges
print(discharges.head(5).to_markdown())

census = pd.read_csv('/Users/brittanykusi-gyabaah/Desktop/GitHub/data-enrichment/data/adi-download/US_2019_ADI_Census Block Group_v3.1.txt')
census.to_csv ('/Users/brittanykusi-gyabaah/Desktop/GitHub/data-enrichment/data/adi-download/US_2019_ADI_Census Block Group_v3.1.txt', index=None)
census
print(census.head(5).to_markdown())

## enrich Discharge table with ADI national rankings
list(discharges.columns)
list(census.columns)
discharges_simple = discharges[['Hospital County', 'Facility Id', 'Zip Code - 3 digits', 'Length of Stay']]
census_simple = census[['FIPS']]

combined_df = discharges_simple.merge(census_simple, how='left', left_on='Facility Id', right_on='FIPS')

combined_df.head(50)
