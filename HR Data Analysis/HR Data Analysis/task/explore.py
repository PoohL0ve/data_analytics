import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution


'''if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.'''

    # write your code here
# Read the data
a_office = pd.read_xml('A_office_data.xml')
b_office = pd.read_xml('B_office_data.xml')
hr_office = pd.read_xml('hr_data.xml')

# convert to Data Frame
a_office_df = pd.DataFrame(a_office)
b_office_df = pd.DataFrame(b_office)
hr_office_df = pd.DataFrame(hr_office)

# change the index
a_index = 'A' + a_office_df['employee_office_id'].astype(str)
a_office_df.set_index(a_index, inplace=True)

b_index = 'B' + b_office_df['employee_office_id'].astype(str)
b_office_df.set_index(b_index, inplace=True)

hr_index = hr_office_df['employee_id'].astype(str)
hr_office_df.set_index(hr_index, inplace=True)

# Place the indexes in list and print
list_a = list(a_office_df.index)
list_b = list(b_office_df.index)
list_hr = list(hr_office_df.index)


# functions to join the datasets
def join_offices(off_1, off_2):
    new_office = pd.concat([off_1, off_2])
    # new_office.reset_index(drop=True, inplace=True)
    """column_names = new_office.columns
    print(list(column_names))
    print(new_office.head())"""
    return merge_offices(new_office, hr_office_df)


# check_office = join_offices(a_office_df, b_office_df)


def merge_offices(off_ab, off_hr):
    one_office = off_ab.merge(off_hr, left_index=True, right_index=True, indicator=True)
    one_office.sort_index(inplace=True)
    one_office.drop(columns=['employee_id', 'employee_office_id', '_merge'], inplace=True)
    final_index = list(one_office.index)
    final_columns = list(one_office.columns)
    #print(final_index)
    #print(final_columns)
    # print(count_bigger_5(one_office))
    return one_office

   # top_ten(one_office)


def top_ten(data_sheet):
    sorted_departments = data_sheet.sort_values(by='average_monthly_hours', ascending=False)
    top_departments = list(sorted_departments['Department'].head(10))
    print(top_departments)

    # Find total number of project for low-salary IT
    low_salary = sorted_departments[sorted_departments.Department == 'IT']
    it_dept = low_salary.loc[:, ['number_project', 'salary']]
    low_sal_it = it_dept[it_dept.salary == 'low']
    total_project = list(low_sal_it['number_project'])
    print(sum(total_project))

    # last_evaluation and satisfaction_level for A4, B7064, and A3033
    columns_eval = ['last_evaluation', 'satisfaction_level']
    all_values = []
    a_4 = data_sheet.loc['A4', columns_eval]
    a_4_list = [float(a_4.iloc[0]), float(a_4.iloc[1])]
    all_values.append(a_4_list)

    b_7 = data_sheet.loc['B7064', columns_eval]
    b_7_list = [float(b_7.iloc[0]), float(b_7.iloc[1])]
    all_values.append(b_7_list)

    a_3 = data_sheet.loc['A3033', columns_eval]
    a_3_list = [float(a_3.iloc[0]), float(a_3.iloc[1])]
    all_values.append(a_3_list)
    print(all_values)


def count_bigger_5(employee):
    big_5 = employee[employee['number_project'] > 5]
    return big_5.shape[0]


# Group by 'left' column and calculate the required metrics
single_office = join_offices(a_office_df, b_office_df)
# print(list(single_office.columns))

# Employees that left the company
left_comp = single_office[single_office['left'] == 1]
# Employees that stayed
stay_comp = single_office[single_office['left'] == 0]

# Median projects worked on for both groups and count > 5
left_median_projects = float(left_comp['number_project'].agg('median'))
stay_median_projects = float(stay_comp['number_project'].agg('median'))
left_more5 = count_bigger_5(left_comp)
stay_more5 = count_bigger_5(stay_comp)

# Mean and median of time spent at the company
left_time_mean = float(left_comp.time_spend_company.agg('mean').round(2))
stay_time_mean = float(stay_comp.time_spend_company.agg('mean').round(2))
left_time_median = float(left_comp.time_spend_company.agg('median'))
stay_time_median = float(stay_comp.time_spend_company.agg('median'))

# Average work accidents of both sets
left_avg_work = float(left_comp.Work_accident.agg('mean').round(2))
stay_avg_work = float(stay_comp.Work_accident.agg('mean').round(2))

# Mean of last evaluation
left_eval_mean = float(left_comp.last_evaluation.agg('mean').round(2))
stay_eval_mean = float(stay_comp.last_evaluation.agg('mean').round(2))

# Standard deviation
left_std = float(left_comp.last_evaluation.agg('std').round(2))
stay_std = float(stay_comp.last_evaluation.agg('std').round(2))

# dictionary results
results = {
    ('number_project', 'median'): {0: stay_median_projects, 1: left_median_projects},
    ('number_project', 'count_bigger_5'): {0: stay_more5, 1: left_more5},
    ('time_spend_company', 'mean'): {0: stay_time_mean, 1: left_time_mean},
    ('time_spend_company', 'median'): {0: stay_time_median, 1: left_time_median},
    ('Work_accident', 'mean'): {0: stay_avg_work, 1: left_avg_work},
    ('last_evaluation', 'mean'): {0: stay_eval_mean, 1: left_eval_mean},
    ('last_evaluation', 'std'): {0: stay_std, 1: left_std}
}

# Final Stage of the Project
# Merged dataFrame
data_merge = join_offices(a_office_df, b_office_df)
# print(list(data_merge.columns))
# first pivot table
department_pivot = data_merge.pivot_table(
    index='Department',
    columns=['left', 'salary'],
    values='average_monthly_hours',
    aggfunc='median'
)
# print(department_pivot)
department_filtered = department_pivot[
    (department_pivot[0, 'high'] < department_pivot[0, 'medium']) |
    (department_pivot[1, 'low'] < department_pivot[1, 'high'])
]
department_filtered.round(2)
# print(department_filtered.round(2))

# second table
time_spend = data_merge.pivot_table(
    index='time_spend_company',
    columns='promotion_last_5years',
    values=['satisfaction_level', 'last_evaluation'],
    aggfunc= ['min', 'max', 'mean']
)
#time_spend.columns = ['_'.join(map(str, col)).strip() for col in time_spend.columns.values]
time_spend.round(2)
# print(list(time_spend.columns))
time_filtered = time_spend[
    time_spend[('mean', 'last_evaluation', 0)] > time_spend[('mean', 'last_evaluation', 1)]
]
# time_filtered.round(2)
# print(time_filtered.round(2))
# Print as dictionaries
depart_dict = department_filtered.round(2).to_dict()
time_dict = time_filtered.round(2).to_dict()
print(depart_dict)
print(time_dict)
