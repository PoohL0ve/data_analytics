"""
    Box plots or box-and-whisker plots used quartiles to represent data distributions.
        Useful arguments:
            vert: set False for horizontal display
            labels: sets the label for each dataset
            showmeans: set to True shows the mean values as a triangle
            meanline: Ture with showmeans sets the mean of a line
            boxprops, medianprops, meanprops. whiskerprops, capprops,
            and flierprops: set the properties of the box, median, mean, whiskers, caps,
            outliers.

            patch_artist=True/False?

            The setprop can be used in a loop: plt.setp(plot[prop], color, linewidth)

    A violin plot is a mixture of a box-plot and a histogram, where it also shows
    the statistics of mean, median, and inter-quartile. It is great for comparing
    distributions for multiple groups.
"""
import matplotlib.pyplot as plt
import pandas as pd
"""data2021 = [0, 20, 20, 50, 85, 20, 20, 20, 70, 90, 10, 0]
fig, axes = plt.subplots()

axes.set_title('Violin plot')
xticklabels = ['Year 2021']
axes.set_xticks([1])
axes.set_xticklabels(xticklabels)
axes.set_ylabel("Annually Sales in percentage")

sales=plt.violinplot(data2021, showextrema=True, showmeans=True, showmedians=True, quantiles=[0.25, 0.75, 0.9])
sales['cmeans'].set_color('m')
sales['cmedians'].set_color('g')

plt.show()

# pandas has its own data visualisation tool
# df.plot(kind='hist'): histogram: it can be used with value_counts().plot()
# Scatter: df.plot(x='Economy (GDP per Capita)', y='Happiness Score', kind='scatter')
"""
data_15 = pd.read_csv('2015.csv')
data_df = pd.DataFrame(data_15)
# data_df.plot(y=['Family', 'Freedom', 'Trust (Government Corruption)'], kind='box', showmeans=True)
# data_df.plot(x='Region', y='Country', kind='bar')
data_df['Region'].value_counts().plot(kind='bar')
plt.show()
print(list(data_df.columns))