#!/usr/bin/env python

'''
Program for bar plot for the crimes occurring on friday after 7 PM

Larceny/Theft have the highest occurance on friday nights
'''
import pandas as pd
import matplotlib.pyplot as plt


try:
	df = pd.read_csv('C:\\Users\\Jen\\Desktop\\train.csv', parse_dates=['Dates'])
except (IOError, OSError) as e:
	print("check file path and location!")

#making new columns by parsing the datetime ... gives hour of the day
df['Hour'] = df['Dates'].map(lambda x: x.hour)
df['Minutes'] = df['Dates'].map(lambda x: x.minute)

colors = ['b', 'r', 'g', 'y', 'k']
	
def plotting(dfd):
	try:
		
		bar   = dfd.plot(
							kind='barh',
							fontsize=10,
							figsize=(10,16),
							stacked=False,
							width=1, 
							color=colors
		)
		
	except Exception as e:
		print (e, "Recheck bar plot parameters!")
	else:
		plt.title("Crimes occuring on Friday after 7PM")
		bar.figure.savefig("Crimes_on_friday.png")
		plt.show()
		

def sorting_grping(fre):
	try:
		df1 = df[(df['DayOfWeek'] == 'Friday')] #crimes which occured on friday
		
		df2 = df1[(df1['Hour'] > 19)] #selecting time after 7PM on fridays
		df3 = df2[['Category', 'DayOfWeek']] # making a dataframe with just two columns for plotting
			
		grp = df3.groupby('Category') #grouping by category to determine the number of each type crime occurred
		freq = grp.size()
		freq.sort(ascending=True, inplace=True) #sorting them by size

	except TypeError as ty:
		print("Empty dataframe...recheck dataframe!")
	except Exception as e:
		print(e, "Check columns!")
	else:
		
		plotting(freq[slice(-1, - fre, -1)])
		testing_pandas(freq[slice(-1, - fre, -1)])



def testing_pandas(dff):
	try:
		if (dff.empty == False): #checking if dataframe is empty
			print ("Test passed!")
	except Exception as e:
		print(e, "Failed!..Recheck!")
		
		
if __name__ == "__main__":
	sorting_grping(fre=0)