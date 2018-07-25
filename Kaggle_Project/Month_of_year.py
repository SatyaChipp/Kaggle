#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt 

def month_of_year():
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
		df['MonthOfYear'] = df['Dates'].map(lambda x: x.month)

		dic = {1: "January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

		df['MonthOfYear'] = df['MonthOfYear'].map(lambda x: dic[x]) # mapping the month names to the column values
	
	except (ValueError, TypeError, KeyError, IndexError) as e:
		print (e)
	except Exception as g:
		print(g)
	else:
		df3 = df[['Category','MonthOfYear']].groupby(['MonthOfYear']).count()
		print (df3.sort('Category', ascending=False)) #shows us the number of crimes occurring by month
		'''OCTOBER has the highest crime rate..Halloween month!
		December has the lowest crime rate, it could be because of the holiday season and fewer police officers on duty or the delay in reporting due to the holidays
		'''
		df3.plot(y='Category', label='Counts of crimes', figsize=(15,10))
		plt.title("Number of Crimes by Month")
		plt.xlabel("Month of the year")
		plt.ylabel("Number of crimes")
		plt.savefig("Crimes by Month of the year.png")
		plt.show()
		testing_pandas(df3)
		
		
def testing_pandas(dff):
	try:
		if (dff.empty == False): #checking if dataframe is empty
			print ("Test passed!")
	except Exception as e:
		print(e, "Failed!..Recheck!")


if __name__ == "__main__":
	month_of_year()
	
	