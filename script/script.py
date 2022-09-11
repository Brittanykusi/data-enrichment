import pandas as pd

######################
## load in datasets ##
######################

discharges = pd.read_csv('/Users/brittanykusi-gyabaah/Desktop/GitHub/data-enrichment/data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
discharges
discharges.dtypes
discharges1 = discharges.astype(str)
discharges1.dtypes

# convert .txt to .csv
census = pd.read_csv('/Users/brittanykusi-gyabaah/Desktop/GitHub/data-enrichment/data/adi-download/US_2019_ADI_Census Block Group_v3.1.txt')
census.to_csv ('/Users/brittanykusi-gyabaah/Desktop/GitHub/data-enrichment/data/adi-download/US_2019_ADI_Census Block Group_v3.1.txt', index=None)
census
census.dtypes
census1 = census.astype(str)
census1.dtypes
census1

# display df in formatted manner 
print(discharges.head(5).to_markdown())
print(census.head(5).to_markdown())



#######################################################
## enrich Discharge table with ADI national rankings ##
#######################################################

# list column names 
list(discharges.columns)
list(census.columns)

# create smaller datasets 
discharges_simple = discharges1[[ 'Facility Id', 'Zip Code - 3 digits']]
census_simple = census1[[ 'FIPS', 'ADI_NATRANK']]

# merge datasets 
combined_df = discharges_simple.merge(census_simple, how='left', left_on='Facility Id', right_on='FIPS')

# display dataset + save dataset as csv
combined_df





