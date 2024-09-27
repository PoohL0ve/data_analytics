import pandas as pd

# GitHub repository that contains Palmer Penguins dataset
#df = pd.read_csv('hyperskill-dataset-103430346.txt')
#penguin_set = pd.DataFrame(df)
# print(list(penguin_set.columns))

# describe() allows you to print the statistics for columns
# with mean(), when accessing certain axis uses numeric_only=True

# finding the mean of R and M labels using the null_deg column
#r_columns = penguin_set.loc[penguin_set['labels'] == 'R', 'null_deg']
#r_mean = r_columns.median().round(3)

#m_columns = penguin_set.loc[penguin_set['labels'] == 'M', 'null_deg']
#m_mean = m_columns.median().round(3)

# print(f'M = {m_mean} R = {r_mean}')
# print(penguin_set.describe())

# example using agg with a dictionary
'''example_agg = penguin_set.agg({
    'sixty_deg': ['mean', 'median'],
    'straight_angle': ['mean', 'median']
})'''
# print(example_agg)
# agg also allow you to use your own function, where you pass parameters
# it blends well with the groupby() method, it has a dropna value (True/False)
# the as_index can be set to False
# print(penguin_set.groupby(['labels', 'twofourty_deg']).agg({'null_deg': 'median'}))

# The agg() function can take function names as string, dictionaries,
# lists, and built in function like sum() as sum or numpy.sum

# the pivot method allows you to reshape the data frame; it can be used with
# pandas or by itself on the data frame: pd.pivot(df, index='year', columns='month', values='passengers'
# It allows the columns to change by the values in a specific column
# reshape = penguin_set.pivot(index='labels', columns='null_deg', values='ninety_deg')
# print(reshape)

# the pivot_table() can take the aggfunc argument as an aggregator for duplicates
# handles reshaping better than pivot()
# multi-index and multi-columns can be passed with []
# The melt() method allows the df to be flattened
# df.melt(id_vars='origin'(Keeps as is), value_var=df.columns[-3:1] (reshapes)
# df.melt(var_name='Name', var_value='Value', ignore_index=False)
hyper_set = pd.read_csv('hyperskill-dataset-103472802.txt')
hyper_df = pd.DataFrame(hyper_set)
pivot_hyper = hyper_df.pivot_table(index='labels', aggfunc='mean')
# print(pivot_hyper)
rocks_mean = round(pivot_hyper.loc['R', 'null_deg'], 2)
# print(rocks_mean)

quiz = pd.read_csv('hyperskill-dataset-103681403.txt', index_col='Name')

'''
 Handling missing values in pandas
 df.isnull() - returns True or False values for NaNs
 Proportion to define NaNs: df.isnull().sum() / df.shape[0]: it divides
 ...it by the number of rows to give a proportion of the columns
 df.isnull().any(): shows if there are missing values or not
 Machine learning models cannot work with missing values, therefore, they need
 to be removed: df.dropna(axis=1, inpplace=True)
'''
# Deleting missing rows
missing = pd.read_csv('hyperskill-dataset-103684507.txt')
missing_df = pd.DataFrame(missing)
first = missing_df.shape[0]
missing_df.dropna(axis=0, inplace=True)
second = missing_df.shape[0]
# print(f'{first} {second}')
# Counting missing values in columns
col_miss = pd.read_csv('hyperskill-dataset-103684783.txt')
col_miss_df = pd.DataFrame(col_miss)
# print(col_miss_df.isnull().sum())
# Count missing columns
count_miss = pd.read_csv('hyperskill-dataset-103685036.txt')
count_miss_df = pd.DataFrame(count_miss)
# print(count_miss_df.isnull().any().sum())
'''
    the thresh= attribute of the dropna() method, takes an integer and deletes.
    rows or column that have more NaN values than it specifies
    Example: df.dropna(axis=1, thresh=10, inplace=True)
    The fillna method can fill NaN values with frequently used values, median,
    mean, or some random value:
        data["dist2subway"] = data.groupby("district", group_keys=False)["dist2subway"].apply(
        lambda x: x.fillna(x.mean()))
    The fillna method can also take the inplace=True attribute
    Use median when there's outliers, use mean when there isn't
'''
# Replace the mode value
replace_mode = pd.read_csv('hyperskill-dataset-103685282.txt')
replace_mode_df = pd.DataFrame(replace_mode)
# find the mode of the location column
location_mode = replace_mode_df['location'].mode()[0]
# replace_mode_df['location'].fillna(location_mode, inplace=True)
# print(replace_mode_df.tail(5))
# Drop the column if it has more than 7 NaNs else replace value
apartment = pd.read_csv('hyperskill-dataset-103685622.txt')
df_apartment = pd.DataFrame(apartment)
# Columns: 'brick', 'floor', 'totsp', 'price'
df_apartment.dropna(axis=1, thresh=7, inplace=True) # deletes the column with more than 7 NaNs
print(df_apartment.isnull().sum())
median_value = df_apartment['price'].median()
df_apartment.fillna(median_value, inplace=True) # fills NaN values with the median_value
print(df_apartment.head(5))

