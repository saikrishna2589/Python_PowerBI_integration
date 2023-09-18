# -*- coding: utf-8 -*-
"""Machine Learning in PowerBI

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O4p1SC-KqnfkH9xJdiWFO3D7-0ejUOOf

# **Machine Learnign Models in PowerBI**

  1.Define the problem and the Model
  2.Data Exploration & Preprocessing
  3.Create the Model
  4.Train the Model

> Indented block


  5.Test the Model
  6.Save the Mode
  7.Import the Model into PowerBI
"""

import pandas as pd

"""# New Section"""

car_sale_price=pd.read_csv("car data.csv") #using pandas to read csv and data is read in a dataframe (2D)



car_sale_price.head()

car_sale_price.info()

df=car_sale_price

df.info()

# profile Pandas data
pandas_profiling.ProfileReport(df)

df.corr()

import seaborn as sns

import seaborn as sns
heatmap_corr=sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)

# counting the values of Transmission column
df['Transmission'].value_counts()

df['Year'].value_counts()

df['Owner'].value_counts()

df['Seller_Type'].value_counts()

# finding duplicate rows
duplicate_rows=df.duplicated()

duplicate_rows

# finding duplicate row
duplicate_rows[duplicate_rows]

df=df.drop_duplicates()

df.duplicated()

df[df.duplicated()]

# drop car names as it has too many different names
df=df.drop('Car_Name',axis=1)

df

#Create Dummy Variables from our Categorical Features
d_df=pd.get_dummies(df)

d_df.head()

"""# **Model Creation**"""

#set our target variable
y=d_df['Selling_Price']
X=d_df.drop('Selling_Price',axis=1)

d_df

# bring our model and train test split

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

X.shape

X_train.shape

X_test.shape

y_train.shape

y_test.shape

y_train

X_test

X_train

model=LinearRegression()

model.fit(X_train,y_train)

predictions=model.predict(X_test)

predictions

"""# Test the Model"""

from sklearn.metrics import mean_squared_error,r2_score

r2_score(y_test,predictions)

from sklearn.model_selection import cross_val_score
scores=cross_val_score(model,X,y,cv=5)

scores

#using mean-squared error  as evaluation metric instead of default cross_val_score scoring metric,which i think is R-square.

mean_squared_error(y_test,predictions)



"""# Save the Model"""

import pickle

#save the model to disk

file=open('model.pkl','wb')
pickle.dump(model,file)
file.close()

# Predict on all of the data as we are convinced model is good.
df['predictions']=model.predict(X)

df.head()

"""# Visualisation"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
sns.kdeplot(data=df,x='predictions',shade=True,label='predictions')
sns.kdeplot(data=df,x='Selling_Price',shade=True,label='Selling_Price')
plt.legend()
plt.show()



"""# AUTOML Approach with PYCARET"""

pip install pycaret

#Load in the pycaret library-Automated ML
from pycaret.regression import *

pip install pycaret[full]

from pycaret.regression import *

# in Pycarat, we need to tell what the categorical variables are. similar to what we did using pandas get_dummies

df.select_dtypes('object').columns

#isolate the categorical features
cat_features=['Fuel_Type', 'Seller_Type', 'Transmission']

df['Selling_Price']



"""Pycaret giving issues so using Jupyter notebook for this module"""