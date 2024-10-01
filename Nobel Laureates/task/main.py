"""
    Perform data analysis on data containing
    information on Nobel Prize winners.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data to the program
load_data = pd.read_json('nobel_laureates.json')
nobel = pd.DataFrame(load_data)

# check for duplicates
same_value = nobel.duplicated()
# print(False)

# Removes rows that have missing values using the gender column
nobel.dropna(subset='gender', inplace=True)

# Re-index the frame and remove the old index
nobel.reset_index(drop=True, inplace=True)

# Extract the first 20 rows for the country and name columns
column_names = list(nobel.columns)  # 2, 7
country_name_20 = nobel.iloc[:20, [2, 7]]

# Stage 2: Correct the birth-places
# Extract list of countries from place_of_birth
nobel['place_of_birth'] = nobel['place_of_birth'].apply(
    lambda country: country.split(',')[-1].strip()
    if country and ',' in country else None
)

# Fill the empty values in the born_in column with values of the previous step
nobel['born_in'] = nobel['born_in'].replace('', pd.NA)
nobel['born_in'] = nobel['born_in'].fillna(nobel['place_of_birth'])

# Remove rows with NaNs in born_in column and re-index the column
nobel = nobel[~nobel['born_in'].isin([pd.NA, 'nan', None])]
nobel.reset_index(drop=True, inplace=True)

# replace appropriate names with the USA and UK
nobel['born_in'] = nobel['born_in'].replace({
    'US': 'USA',
    'U.S.': 'USA',
    'United States': 'USA',
    'United Kingdom': 'UK'
})
# List of born_in values
born_in_list = list(nobel.born_in)

# Stage 3: Correct the Dates


# function to extract only the year from different formats
def extract_year(value):
    if pd.isna(value):
        return None

    date_of_birth = value.strip()

    if ',' in date_of_birth:
        year = date_of_birth.split(',')[-1].strip()
    elif '-' in date_of_birth:
        parts = date_of_birth.split('-')
        if len(parts[0]) == 4:  # Assuming YYYY-MM-DD format
            year = parts[0].strip()
        else:  # Assuming DD-MM-YYYY format
            year = parts[-1].strip()
    elif ' ' in date_of_birth:
        year = date_of_birth.split(' ')[-1].strip()
    else:
        year = date_of_birth.strip()

    return year


# New column with the birth year of nobel winners
nobel['year_born'] = nobel['date_of_birth'].apply(extract_year)
nobel['year_born'] = pd.to_numeric(nobel['year_born'], errors='coerce')
# Age of winning the prize
nobel['age_of_winning'] = nobel['year'] - nobel['year_born']

# Stage 4: Plot a pie chart of the born_in
extract_value_count = nobel.born_in.value_counts()
test_25 = dict(extract_value_count)
# Loop to iterate the list
countries_2 = []
count_2 = []
check = 0
for key, value in test_25.items():
    if int(value.item()) >= 25:
        countries_2.append(key)
        count_2.append(value.item())
    elif int(value.item()) < 25:
        check += 1
countries_2.insert(0,'Other countries')
count_2.insert(0, 343)


# pie chart details
def autopct_format(pct, allvalues):
    absolute = int(pct/100.*sum(allvalues))
    return '{:.2f}%\n({:.0f})'.format(pct, absolute)


plt.figure(figsize=(12, 12))
colours = ['blue', 'orange', 'red', 'yellow', 'green', 'pink',
           'brown', 'cyan', 'purple']
explode = [0, 0, 0, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08,]
plt.pie(count_2, labels=countries_2, explode=explode,
       colors=colours, autopct=lambda pct: autopct_format(pct, count_2))
# plt.show()

# Stage 5: Plot a bar chart based on categories for male and females
# Female list: After testing with value counts a category without
# ... a number contained a count of 6; it won't be used
check_categories = nobel.category.value_counts()
categories_full = check_categories[check_categories > 6]
categories_list = categories_full.index.tolist()
# Place list in ascending order
sorted_category = sorted(categories_list)

female_df = nobel[nobel['gender'] == 'female']
male_df = nobel[nobel['gender'] == 'male']
female_count = female_df['category'].value_counts()
male_count = male_df['category'].value_counts()

# Sort the male and female lists
female_sorted = [int(female_count.get(val, 0)) for val in sorted_category]
male_sorted = [int(male_count.get(val, 0)) for val in sorted_category]

# Set up the bar chart
# Set the range for the x_axis
x_axis = np.arange(len(sorted_category))
# Set the figure_size to 10, 10
plt.figure(figsize=(10, 10))

# Create the two bars
plt.bar(x_axis - 0.2, male_sorted, width=0.4, color='blue', label='Males')
plt.bar(x_axis + 0.2, female_sorted, width=0.4, color='crimson', label='Females')

plt.xticks(x_axis, sorted_category)
plt.ylabel('Nobel Laureates Count', fontsize=14)
plt.xlabel('Category', fontsize=14)
plt.title('The total count of male and female Nobel Prize'
          ' winners by category', fontsize=20)

plt.legend()


# Stage 6: Create a set of box plots for the ages in each category
# get the ages for each category

extract_cat = nobel.iloc[:, [1, -1]]
chemistry_ages = extract_cat[extract_cat['category'] == 'Chemistry']
list_chemistry_ages = sorted(chemistry_ages.age_of_winning.tolist())

econ_ages = extract_cat[extract_cat['category'] == 'Economics']
list_econ_ages = sorted(econ_ages.age_of_winning.tolist())

literature_ages = extract_cat[extract_cat['category'] == "Literature"]
list_lit_ages = sorted(literature_ages.age_of_winning.tolist())

peace_ages = extract_cat[extract_cat['category'] == 'Peace']
list_peace_ages = sorted(peace_ages.age_of_winning.tolist())

physics_ages = extract_cat[extract_cat['category'] == 'Physics']
list_physics_ages = sorted(physics_ages.age_of_winning.tolist())

phys_med_ages = extract_cat[extract_cat['category'] == 'Physiology or Medicine']
list_phys_med_ages = sorted(phys_med_ages.age_of_winning.tolist())

all_cat = [age for sublist in [
    list_chemistry_ages, list_econ_ages, list_lit_ages,
    list_peace_ages, list_physics_ages, list_phys_med_ages
] for age in sublist]

# Plot data
data_categories = [list_chemistry_ages, list_econ_ages, list_lit_ages,
                   list_peace_ages, list_physics_ages, list_phys_med_ages, all_cat]

labels = ['Chemistry', 'Economics', 'Literature', 'Peace', 'Physics',
          'Physiology or Medicine', 'All categories']
plt.figure(figsize=(10, 10))

plt.boxplot(data_categories, labels=labels, showmeans=True)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Age of Obtaining the Nobel Prize', fontsize=14)
plt.title('Distribution of Ages by Category', fontsize=20)
plt.show()











