import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {
	'Day': [1, 2, 3, 4, 5, 6],
	'Visitors': [43, 56, 34, 23 ,88, 45],
	'Bounce_Rate' : [23, 45, 56, 20, 35, 24]						


}
#dataframe = stat
stat = pd.DataFrame(web_stats)


#print(stat.head())
#print(stat.tail())
#print(stat.tail(3))
 
#stat2 = stat.set_index('Day') # makes new df with index set as 
#print(stat2.head)

stat.set_index('Day',inplace=True) #modifies dataframe
print(stat.head()) # changes index to new index with inplace

print(stat['Bounce_Rate']) # prints values under key


print(np.array[['Day', 'Bounce_Rate']])