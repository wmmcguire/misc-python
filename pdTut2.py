#pandas i/o
import pandas as pd 

stat = pd.read_csv('ZILLOW-Z11236_ZRISFRR.csv') # read csv file
print(stat.head())
stat.set_index('Date', inplace=True)
stat.to_csv('newcsv.csv')

stat = pd.read_csv('newcsv.csv') # read csv file
print(stat.head())

stat = pd.read_csv('newcsv.csv', index_col=0) # read csv file
print(stat.head())

stat.columns = ['Flossy_HPI']
print(stat.head())

stat.to_csv('newcsv2.csv')
stat.to_csv('newcsv3.csv')

stat = pd.read_csv('newcsv3.csv', names=['Date','Flossy_HPI'], index_col=0)

stat.to_html('example.html')



