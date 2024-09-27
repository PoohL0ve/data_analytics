import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)
# Reading and Loading datasets
general_read = pd.read_csv('general.csv')
prenatal_read = pd.read_csv('prenatal.csv')
sports_read = pd.read_csv('sports.csv')

general = pd.DataFrame(general_read)
prenatal = pd.DataFrame(prenatal_read)
sports = pd.DataFrame(sports_read)

# Renaming the columns for prenatal and sports
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# Concatenating the Datasets into one
all_hospitals = pd.concat([general, prenatal, sports], ignore_index=True)
all_hospitals.drop(columns='Unnamed: 0', inplace=True)
random_rows = all_hospitals.sample(n=20, random_state=30)

# Removing NaN values from the dataset
all_hospitals.dropna(how='all', inplace=True)


# Function to change the gender column values to f or m
def change_value(col):
    if col['gender'] == 'female' or col['gender'] == 'woman':
        col['gender'] = 'f'
    elif col['gender'] == 'male' or col['gender'] == 'man':
        col['gender'] = 'm'
    elif col['hospital'] == 'prenatal':
        col['gender'] = 'f'
    return col


# Apply the method to the DF by accessing the rows
all_hospitals = all_hospitals.apply(change_value, axis=1)
# Fill with 0s: bmi, diagnosis, blood test, ecg, ultrasound, mri,
# ... xray, children, and months
all_hospitals[['bmi', 'children', 'months']] = all_hospitals[[
    'bmi', 'children', 'months']].fillna(0.0)
all_hospitals[['diagnosis', 'mri', 'blood_test', 'ecg', 'ultrasound', 'xray']] = all_hospitals[
     ['diagnosis','mri', 'blood_test', 'ecg', 'ultrasound', 'xray']].fillna('0')

frame_shape = all_hospitals.shape
random2 = all_hospitals.sample(n=20, random_state=30)

# Statistics: Answer the questions
# Hospital with the most patients
count_hospitals = all_hospitals.hospital.value_counts()
hospital_answer = f'The answer to the 1st question is general'


# Share of patients that suffer from stomach issues in the general hospital: 461
stomach_general = all_hospitals[
    (all_hospitals.diagnosis == 'stomach') & (all_hospitals.hospital == 'general')
]
stomach_share = round((((stomach_general.shape[0] / 461) * 100) / 100), 3)
stomach_answer = f'The answer to the 2nd question is {stomach_share}'


# Share of patients with dislocations in the sports hospital
sports_dislocation = all_hospitals[
    (all_hospitals.diagnosis == 'dislocation') &
    (all_hospitals.hospital == 'sports')
]
sport_count = all_hospitals.hospital.value_counts().loc['sports']
dislocation_sports_share = round((((sports_dislocation.shape[0] / sport_count) * 100) / 100), 3)
dislocation_answer = f'The answer to the 3rd question is {dislocation_sports_share}'


# Differences in the median ages of patients in the general and sports hospitals
general_age = all_hospitals[
    (all_hospitals.hospital == 'general') & all_hospitals.age
]
general_median = general_age['age'].median().round(3)
sports_age = all_hospitals[(all_hospitals.hospital == 'sports') & all_hospitals.age]
sports_median = sports_age['age'].median().round(3)
difference = general_median - sports_median
difference_answer = f'The answer to the 4th question is {difference}'


# Hospital that took the most blood_test and the amount

general_blood = all_hospitals[
    (all_hospitals.hospital == 'general') & (all_hospitals.blood_test == 't')
]
blood_general = general_blood.blood_test.count()

prenatal_blood = all_hospitals[
    (all_hospitals.hospital == 'prenatal') & (all_hospitals.blood_test == 't')
]
blood_prenatal = prenatal_blood.blood_test.count()

sports_blood = all_hospitals[
    (all_hospitals.hospital == 'sports') & (all_hospitals.blood_test == 't')
]
blood_sports = sports_blood.blood_test.count()
blood_test_answer = f'The answer to the 5th question is prenatal, {blood_prenatal} blood tests'

# Visualisations
# Find the mode range of age
all_hospitals.age.plot(kind='hist')  # 15 - 35
plt.show()

# Find the most common diagnosis
all_hospitals.diagnosis.value_counts().plot(kind='pie')  # pregnancy
plt.show()

# Create a violin-plot of the heights of patients
height_dist = all_hospitals.height
plt.violinplot(height_dist, showmeans=True, showmedians=True, showextrema=True)
plt.show()

# Answers to the questions
first = 'The answer to the 1st question: 15-35'
second = 'The answer to the 2nd question: pregnancy'
third = ('The answer to the 3rd question: Some values of height were not reported'
         ' or those height ranges do not correspond to patients')
print(f'{first}\n{second}\n{third}')