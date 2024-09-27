"""
    Practice with the apply method for dataframes.
    To use the method on rows, set the axis=1
    apply(): applies a function to rows or columns, result is a DF or Series depending
    on the resulting shape;
    applymap(): applies a function to each value, result is the same shape;
    map(): applies a function to elements in a Series, result is the same shape;
    np.broadcast(): similar to apply(funct, result_type='broadcast')

    To check the progress install tqdm and set tqdm.pandas, and change apply to
    progress_apply()
    Example:
        tqdm.pandas()
        result = df[['Tax', 'Income']].progress_apply(check_mean, result_type=broadcast)
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({
   'Name': ['John', 'Jane', 'Bob', 'Mary', 'Ivan'],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Moscow'],
   'Age': [32, 25, 47, 19, 45],
   'Income': [55000, 72000, 89000, 41000, 45000]
})
print(df.head(3))


# Method that changes the rows and creates new columns
def change_row(row):
    row['Name'] = row['Name'].upper()
    row['City'] = row['City'].lower()
    row['Age'] = row['Age'] + 10
    row['Income'] = row['Income'] * 1.1
    return row


df = df.apply(change_row, axis=1)  # applies the method to the rows
# print(df.head(3))


# Add a new column
def add_tax(row):
    if row['Income'] > 60000:
        tax = row['Income'] * 0.25
    else:
        tax = row['Income'] * 0.1
    return tax  # adds a new column to the df


df['Tax'] = df.apply(add_tax, axis=1)
# print(df.head(3))


# suffixes for values can be added for a specific column
def add_suffix(col, suffix):
    return col + suffix


df['Name'] = df['Name'].apply(add_suffix, suffix='_Happy')
# for numerous columns use df[col1, col2 ...]
# print(df.head(3))

# Using apply with built-in functions
df_nums = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df_nums['MaxValue'] = df_nums.apply(max, axis=1)  # max value in each row
print(df_nums)

# Using apply with lambda functions
df['Name'] = df['Name'].apply(lambda e: e+'_People')

# Using apply with numpy functions
df['Tax-Sqrt'] = df['Tax'].apply(np.sqrt).round(2)
print(df.head(3))
# Other panda methed like isnull can be use: apply(pd.isnull)
# The result_type parameter can take expand, reduce, and broadcast


# expand returns a DF or Series containing the output of the function to each element
def calculate_tax(income, tax):
    return pd.Series({'Tax rate': (income / tax) * 100, 'Tax rank': 10000 - tax})


result_tax = df[['Income', 'Tax']].apply(lambda x: calculate_tax(*x), axis=1, result_type='expand')
# print(result_tax)

# reduce returns a reduced single value of the output
def sum_row(row):
    return row['Income'] + row['Tax']


result_income_sum = df.apply(sum_row, result_type='reduce', axis=1)
# print(result_income_sum)


# broadcast returns the frame with the result of the function repeated for each element
def mean_of_column(col):
    return col.mean()


result = df[['Income', 'Tax']].apply(mean_of_column, result_type='broadcast')

"""
    Summary statistics is needed when we need to compare datasets or 
    data grouped by categories.
    Counting process:
        Non-Null values in a column: df.columnName.count()
        Null values in a column: df.columnName.isna().sum(): isna() returns True for null values
        Number of cells/rows in a column: df.shape[0]
        Unique values in a column: df.columnName.nunique()
    Frequency of each unique value:
        df.columnName.value_counts() - The result is a Series, no need to group
        Find specific entries in the result: df.columnName.value_counts().loc[['s', 'b']]
    A list of unique values: df.columnName.unique() - returns a Numpy array (iterable)
        Example: [('The ' + species + ' penguin') for species in df.species.unique()]
"""
# Check how many Rs
check_r = pd.read_csv('hyperskill-dataset-103729854.txt')
check_r_df = pd.DataFrame(check_r)
number = check_r_df.labels.value_counts().loc['R']
print(number)
