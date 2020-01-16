import pandas as pd # standard
import matplotlib.pyplot as plt #standard
from matplotlib import style #style graph
import numpy as np
style.use('ggplot')



while True:
	web_stats = { 
		'Day': [1, 2, 3, 4, 5, 6],
		'Visitors' : [43, 53, 34, 45, 64, 34],
		'Bounce_Rate' : [65, 72, 62, 64, 54, 66]
	
	}

	stats = pd.DataFrame(web_stats) # df - "data frame"
	#Turns dictionary into data frame

	plt.plot([web_stats['Day'], web_stats['Visitors']])
	plt.xlabel('Days')
	plt.ylabel('Amount of Visitors')
	plt.show()
	exit()



	#print(stats.Day.tolist()) # converts colmn 


	#print(np.array(stats[['Visitors', 'Day']])) #puts data into a list of lists

	#stats2 = pd.DataFrame(np.array(stats[['Visitors', 'Day']]))
	#print(stats2)

