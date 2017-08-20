import pandas as pd
import math,time,datetime,pickle
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import csv
from sklearn.metrics import r2_score

df=pd.read_csv('train.csv')


#print(df.head())

X=np.array(df.drop(['medv','ID'],1))
X=preprocessing.scale(X)
y=np.array(df['medv'])

#X_train, X_test, y_train, y_test=cross_validation.train_test_split(X, y, test_size=0.2)

clf= LinearRegression(n_jobs=-1)

clf.fit(X, y)
# accuracy=clf.score(X_test,y_test)

# print(accuracy)

p=pd.read_csv('test.csv')

for i in range(len(p)):
    predict_me=np.array(X[i].astype(float))
    #print "before:", predict_me
    predict_me=predict_me.reshape(-1,len(predict_me))
    #print "after:", predict_me
    prediction=clf.predict(predict_me)

    with open('a.csv', "a") as file:
        writer = csv.writer(file)
        writer.writerow(prediction)



