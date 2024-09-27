"""
    The matplotlib has numerous modules like 'matplotlib.table' for creating tables
    and matplotlib.colorbar for scalar colors. The matplotlib.pyplot is for creating
    plots.
"""
import matplotlib.pyplot as plt
import numpy as np

# Explicitly creating figures and axes
# fig, ax = plt.subplots()
# x = np.linspace(0, 10, 200)
# y = np.sin(x) + x
# ax.plot(x, y)
# plt.show() use instead of fig.show()
# plt.figure() is another way to create a figure
"""
    The settings of the plot can be altered
    Length and width: plt.subplots(figsize=(15, 10))
    Title of figure: fig.suptitle("Whatever", fontsize=40)
    Styling the color, the line style and line width:
        ax.plot(x, y, c='blue', linestyle='dotted', linewidth=4)
        
    Axes settings
        Change the x and y lables: ax.set_xlabel('Happy", fontsize=40)
        The values on the axes can be changed with xaxis and yaxis as values to
        axis parameter: ax.tick_params(axis='both', which='major', labelsize=18)
        
    Closing windows:
        plt.close(fig) or plt.close() to close all windows
        To delete a figure but leave the window open: plt.clf()

# Creating multiple plots
figs, axe = plt.subplots(1, 2, figsize=(16, 8))  # 1, 2 are the rows and columns
ax1, ax2 = axe

x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.cos(x)

# Setting the labels
ax1.set_xlabel('x', fontsize=40)
ax1.set_ylabel('sin x', fontsize=40)

ax2.set_xlabel('x', fontsize=40)
ax2.set_ylabel('cos x', fontsize=40)
# Add padding between plots
figs.tight_layout(pad=4)
ax1.plot(x, y1, c='b', linestyle='dotted', linewidth=4)
ax2.plot(x, y2, c='g', linestyle='dotted', linewidth=4)
# plt.show()
"""
"""
    A histogram uses ranges to display data in bars and is different from a
    bar chart in that it represent numerical data, while a bar chart represents
    categorical data.

weight = [200, 120, 150, 135, 200, 145, 180, 150, 135, 195]
#plt.hist(weight, color='green', edgecolor='white')
#plt.title('Random Weight')
#plt.xlabel('Weight in lbs')
#plt.ylabel('Number of Persons')

# the bins argument specifies how the data can be divided into intervals: integer, list
# It can take string values like auto, rice, sqrt
# To cut of data pass a tuple like (150, 190) to the range argument
#bins = [120, 140, 160, 200]
#plt.hist(weight, bins='auto', color='green', edgecolor='white')
#plt.title('Random Weight')
#plt.xlabel('Weight in lbs')
#plt.ylabel('Number of Persons')
# plt.show()

# We can have multiple plots; include the plt.legend()
my_data = [163, 163, 164, 170, 170, 172, 173, 190]
andy_data = [161, 172, 174, 175, 181, 183, 186, 190]
bins = [160, 170, 180, 190]
names = ["my friends", "Andy's friends"]

plt.hist([my_data, andy_data], bins=bins, label=names)
# The default display is side by side but setting stacked=True can change it
plt.title("Mine and Andy's friends' height")
plt.ylabel("Number of people")
plt.xlabel("Height in cm")

plt.legend()
plt.show()
"""
"""
    Pie charts work great with categorical data and represents each element
    as a percentage. Create plt.pie(data), it has several parameters:
        explode = separates slices: explode=[0.3, 0.2] - percent element wil separate by
        labels = list of strings for each slice, labeldistance = pie label distance
        color(must set shade=True), autopct - labels slices with its numerical value
            autoclt='%.2f'
        shadow - creates a shadow of a slice, startangle - choose starting angle
            startangle=90 counterclock=False: It is counter-clock wise by default
        wedgeprops - tune various parameters, radius - set radius of the circle
            wedgeprops={'width': 0.2}
    To set the title: plt.title(), plt.legend(labels) - creates mapping for elements
"""