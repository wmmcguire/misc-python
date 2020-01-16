import pandas as pd #printing script
import quandl, math #quandl is a database for stock prices. math for mathematical operations.
import numpy as np 
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression



#preprocessing helps with scaling, accuracy, processing speed. tedious but useful.
#cross_validation helps shuffle data, avoiding biased samples. creates testing samples in this case.



df = quandl.get('WIKI/GOOGL')


df = df[['Adj. Open', 'Adj. High', 'Adj. Low','Adj. Close', 'Adj. Volume',]]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change', 'Adj. Volume']]


#print(df.head())
#input()

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.03*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
#print(df.head())



x = np.array(df.drop(['label'],1))
y = np.array(df['label'])
x = preprocessing.scale(x)

df.dropna(inplace=True)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = svm.SVR(kernel='poly')
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)*100

print(accuracy)
input()
















