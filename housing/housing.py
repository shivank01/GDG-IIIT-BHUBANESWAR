import pandas as pd
import math,time,datetime,pickle
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import csv
from sklearn.metrics import mean_squared_error

df=pd.read_csv('train.csv')
X=np.array(df.drop(['medv','ID'],1))
X=preprocessing.scale(X)
y=np.array(df['medv'])

X_train, X_test, y_train, y_test=cross_validation.train_test_split(X, y, test_size=0.2)

clf= LinearRegression(n_jobs=-1)

clf.fit(X_train, y_train)
accuracy=clf.score(X_test,y_test)
#print(accuracy)

p=pd.read_csv('test.csv')

prediction=[]

for i in range(len(p)):
    predict_me=np.array(X[i].astype(float))
    #print "before:", predict_me
    predict_me=predict_me.reshape(-1,len(predict_me))
    
    output = clf.predict(predict_me)

    with open('a.csv', "a") as file:
        writer = csv.writer(file)
        writer.writerow(output)

    prediction.append(clf.predict(predict_me))

prediction = np.array(prediction)
#print(prediction)
MdevMean = np.mean(prediction)

meanList = []
for _ in range(len(prediction)):
	meanList.append(MdevMean)

print(mean_squared_error(prediction, meanList))






