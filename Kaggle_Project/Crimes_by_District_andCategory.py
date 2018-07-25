#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
	

def districtplot():
	try:
		district_names = np.unique(df['PdDistrict'])

		df2 = df[['X','PdDistrict']].groupby(['PdDistrict']).count().rename(columns={'X':'CrimesByDistrict'})
	except (ValueError, TypeError, KeyError, IndexError) as e:
		print (e)
	except Exception as g:
		print(g)
	else:
		
		plt.figure()
		df2.plot(kind='barh', figsize=(25,10), color='k')
		plt.show()
		'''
		Shows us that SOUTHERN district has the highest crime rate
		'''
		plt.savefig('Crimes_byDistricts.png')
		testing_pandas(df2)
		
def catplot():
	try:
		district_names = np.unique(df['PdDistrict'])

		df['event'] = 1
		df3 = df[['PdDistrict', 'Category', 'event']]
		by_category = df3[['PdDistrict','Category','event']].groupby(['PdDistrict','Category']).count().reset_index()
		piv_data = by_category.pivot(index='Category', columns='PdDistrict',values='event').fillna(0) #filling missing values with 0 
		#pivoting to obtain category by district
	except (ValueError, TypeError, KeyError, IndexError) as e:
		print (e)
	except Exception as g:
		print(g)
	else:	
		
		plt.figure()
		piv_data.plot(kind='bar', figsize=(25,10))
		plt.show()
		'''
		Shows us crimes by district
		Bayview and Northern districts seem to have high LARCENY/THEFTS
		Mission has high prostitution and Tenderloin has surprisingly high drug/narcotic crimes
		'''
		plt.savefig('Crimes_by_district_byCategory.png')
		testing_pandas(df3)
		
def testing_pandas(dff):
	try:
		if (dff.empty == False): #checking if dataframe is empty
			print ("Test passed!")
	except Exception as e:
		print(e, "Failed!..Recheck!")

	
	
if __name__ == '__main__':
	districtplot()
	catplot()
