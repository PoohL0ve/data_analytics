"""
    Using Descriptive Analysis to understand the data
    presented about nobel prize winners.
    Objectives:
        - What countries produce the most winners?
        - How do the genders compare?
        - What ages are the most likely to win?
        - Who won the most times?
        - What field is the most dominant?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the json file
nobel = pd.read_json('nobel_laureates.json')
original_shape = nobel.shape  # (1052, 12)

# Clean the Data
# Check for the number of null values
missing_values = nobel.isnull().sum()
# Columns with missing values: date_of_birth, date_of_death, gender,
#... place_of_birth, place_of_death

missing_genders = nobel[
    nobel['gender'].isnull() | (nobel['gender'] == '')
]  # Checks other data points to understand

# Change the column gender to entity to represent all values
nobel['entity'] = nobel['gender']
nobel['entity'] = nobel['entity'].fillna('group')

missing_births = nobel[nobel['date_of_birth'].isnull()]
missing_deaths = nobel[nobel['date_of_death'].isnull()]

# Fill date_of_death with 0 as there are groups that still exist
nobel['date_of_death'] = nobel['date_of_death'].fillna(0)
nobel['place_of_death'] = nobel['place_of_death'].fillna('Still Exists')

fill_idi = nobel[nobel['name'] == 'Institut de Droit International'].index[0]
nobel.loc[fill_idi, 'date_of_birth'] = '9-8-1873'
print(nobel.isnull().sum())
#fill_fsc = 
['Institut de Droit International', 'Friends Service Council', 
 'American Friends Service Committee  (The Quakers)',
   'Amnesty International', 'Médecins Sans Frontières', 
   'Médecins Sans Frontières', 'Pugwash Conferences on Science and World Affairs', 
   'International Atomic Energy Agency']


missing_place_b = nobel[nobel['place_of_birth'].isnull() | (nobel['place_of_birth'] == '')]
print(missing_place_b.head(5))
