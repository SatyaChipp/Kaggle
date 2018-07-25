#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt

def day_of_year():
	try:
		
		df1 = pd.read_csv('C:\\Users\\Jen\\Desktop\\train.csv', parse_dates=['Dates'])
		df2 = pd.read_csv('C:\\Users\\Jen\\Desktop\\test.csv', parse_dates=['Dates'])
	
	except (IOError, OSError) as e:
		print (e, "Check input file path")
	except Exception as r:
		print (r)
	else:
		
		frames = [df1, df2]  
		df = pd.concat(frames) #concat test and train data , because data is split between both and to get the correct estimates in the plots/results
	try:
		df['DayOfYear'] = df['Dates'].map(lambda x: x.day) #  for the day of the year from the dates column
		
		df['HourOfDay'] = df['Dates'].map(lambda x: x.hour) 
		
		df2 = df[['Category', 'DayOfYear']].groupby(['DayOfYear']).count()
		
		df3 = df[['Category', 'HourOfDay']].groupby(['HourOfDay']).count()
	
	except (ValueError, TypeError, KeyError, IndexError) as e:
		print (e)
	except Exception as g:
		print(g)
	else:
		print (df3.sort('Category', ascending=False).head())
		print (df2.sort('Category', ascending=False).head())
		'''
		We can see that highest crime occurance on the first of the month
		Could be reporting differences or because of the salary correlation at the beginning of the month
		Even criminals have to pay rent..
		Its interesting though how crime rates peak on the 1st, after plummeting towards the end of the month
		'''
		
		df2.plot(figsize=(25,10)) 
		plt.title("Crimes peak at the start of the month")
		plt.ylabel('Number of crimes')
		plt.xlabel('Day of year')
		plt.savefig('Distribution_of_Crimes_by_DayofYear.png')
		plt.show()
		df3.plot(figsize=(25,10))
		'''
		Shows us that most crimes occur around 6PM
		'''
		plt.title("Highest crime rate around 6PM")
		plt.ylabel('Number of crimes')
		plt.xlabel('Hour of the Day')
		plt.savefig('Distribution_of_Crimes_by_Hour_of_Day.png')
		
		plt.show()
		testing_pandas(df2)
		testing_pandas(df3)
		
		
def testing_pandas(dff):
	try:
		if (dff.empty == False): #checking if dataframe is empty
			print ("Test passed!")
	except Exception as e:
		print(e, "Failed!..Recheck!")

	
if __name__ == "__main__":
		day_of_year()