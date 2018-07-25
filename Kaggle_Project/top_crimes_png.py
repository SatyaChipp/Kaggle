#!/usr/bin/env python

import sys
import string
import pandas as pd
import numpy as np
import seaborn as sr
import matplotlib.pyplot as plt

# Plotting Options
sr.set_style("darkgrid") #set the background
sr.despine() #to remove the top and right axes spines

palette = (
'Set2', 'husl', 'muted', 'Paired',
'Set1', 'RdGy', 'deep', 'spectral'
)
def bar_plot_col(df, title, filename): #for bar plots
	
	colors_choice = sr.color_palette(np.random.choice(palette), len(df)) #color selection for plots made at random
	try:
		bar   = df.plot(
						kind='bar', #for vertical bar charts
						title=title,
						fontsize=10,
						figsize=(10,16),
						stacked=False,
						width=1,
						color=colors_choice,
		)
	except Exception as e:
		print(e)
	else:
		bar.figure.savefig(filename)
		plt.show()

def top_crimes(df, column, title, pngname, fre=0): #for seaborn plots
	try:
		df.columns = df.columns.map(lambda x: x.lower()) #changing to lower case
		group_column = df.groupby(column) # grouping by values in the column
		freq_column = group_column.size()
		freq_column.index = freq_column.index.map(string.capwords)
		freq_column.sort(ascending=True, inplace=True) #sorting them by size
	except Exception as e:
		print (e)
	else:
		bar_plot_col(freq_column[slice(-1, - fre, -1)], title, pngname)


def read_and_plot():
	try:
	
		df = pd.read_csv('C:\\Users\\Jen\\Desktop\\train.csv', parse_dates=True, index_col='Dates', na_values='NONE')
	except (IOError, OSError) as e:
		print(e, "check input file path!")
	else:
		
		top_crimes(df, 'category',   'Top Crime Categories',        'category.png') #plot by category
		top_crimes(df, 'resolution', 'Top Crime Resolutions',       'resolution.png') #plot by resolutions
		top_crimes(df, 'pddistrict', 'Top areas/districts',  'police.png') #plot by districts... less specific than the location.png
		top_crimes(df, 'dayofweek',  'Top Days of the Week',            'weekly.png') #plot crimes by day of the week
		top_crimes(df, 'address',    'Top Crime Locations(more specific)',         'location.png', fre=20) #plot crimes by locations..more specific
		testing_pandas(df)
		
def testing_pandas(dff):
	try:
		if (dff.empty == False): #checking if dataframe is empty
			print ("Test passed!")
	except Exception as e:
		print(e, "Failed!..Recheck!")

if __name__ == '__main__':
	read_and_plot() #exit the script after plots

