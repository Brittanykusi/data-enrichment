# Data-enrichment

## Task
write python code that will enrich SPARCS.csv with public health information from the Neighborhood Atlas and if you want to, but not manditory, you can choose another dataset of your choice
- The data that you decide to enrich with, should be based/linked to either a zipcode, county, city, or state level to the SPARCS.csv

## Data sets
- For the Neighborhood Atlas, go to: https://www.neighborhoodatlas.medicine.wisc.edu/ register and go to ‘download data’ section on top right-hand side of screen
- For the Hospital Inpatient Discharges (SPARCS) data (.csv), please go to https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/82xm-y6g8 and download the .csv file from the EXPORT -> CSV for Excel format. This is the 2015 NYDOH Hospital Inpatient Discharges (SPARCS de-identified) 2015 information.  

## First steps for script
- https://github.com/Brittanykusi/data-enrichment/blob/f09d189b585d86d004b6a54acb4cc5d5af5f029a/script/script.py#L1

## load in data sets
- copy path from files located on host computer
  -  https://github.com/Brittanykusi/data-enrichment/blob/f09d189b585d86d004b6a54acb4cc5d5af5f029a/script/script.py#L7 
  - https://github.com/Brittanykusi/data-enrichment/blob/f09d189b585d86d004b6a54acb4cc5d5af5f029a/script/script.py#L14-L15
- to view datasets simply run variable name given to said dataset
  - {ex} https://github.com/Brittanykusi/data-enrichment/blob/f09d189b585d86d004b6a54acb4cc5d5af5f029a/script/script.py#L16

## Merge or enrich data
- create smaller datasets to work with
  - https://github.com/Brittanykusi/data-enrichment/blob/f09d189b585d86d004b6a54acb4cc5d5af5f029a/script/script.py#L37-L38
- merge datasets with a left join
  - https://github.com/Brittanykusi/data-enrichment/blob/f09d189b585d86d004b6a54acb4cc5d5af5f029a/script/script.py#L41


