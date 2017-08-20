import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import csv
from sklearn import preprocessing

df=pd.read_csv('xtrain.csv')
#print df.head()

df.drop(['body','name'],1,inplace=True)
df.convert_objects(convert_numeric=True)
#print df.head()
df.fillna(0,inplace=True)

def handle_non_numeric_data(df):
    columns=df.columns.values
    for column in columns:
        text_digit_values={}
        def convert_to_int(val):
            return text_digit_values[val]


        if df[column].dtype!=np.int64 and df[column].dtype!=np.float64:
            columns_contents=df[column].values.tolist()
            unique_elements=set(columns_contents)
            x=0
            for unique in unique_elements:
                if unique not in text_digit_values:
                    text_digit_values[unique]=x
                    x+=1

            df[column]=list(map(convert_to_int,df[column]))

    return df

df=handle_non_numeric_data(df)

#print(df.head())



test=pd.read_csv('xtest.csv')
test.drop(['body','name'],1,inplace=True)
test.convert_objects(convert_numeric=True)
#print df.head()
test.fillna(0,inplace=True)
test=handle_non_numeric_data(test)
X=np.array(test).astype(float)
X=preprocessing.scale(X)



clf=KMeans(n_clusters=2)
clf.fit(X)



for i in range(len(X)):
    predict_me=np.array(X[i].astype(float))
    #print "before:", predict_me
    predict_me=predict_me.reshape(-1,len(predict_me))
    #print "after:", predict_me
    prediction=clf.predict(predict_me)
    with open('a.csv', "a") as file:
        writer = csv.writer(file)
        writer.writerow(prediction)


    




























