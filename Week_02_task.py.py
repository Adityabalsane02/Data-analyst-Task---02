
import pandas as pd


data = pd.read_csv("E:\\Main flow Internship data analysis\\task-02/01.Data Cleaning and Preprocessing.csv")

type(data)
print(data)
data.info
print(data)
print(data.head())
data.describe()
data = data.drop_duplicates()
print(data)
data.isnull()
data.isnull().sum()
data.isnull().sum().sum()
data2 = data.fillna(value=0)
print(data2)
data3 = data.fillna(method ='pad')
print(data3)
data4 = data.fillna(method='bfill')
print(data4)
import numpy as np
data2.columns
data2.drop(['Observation'],axis =1,inplace=True)
data2.columns
print(data2)

Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR = Q3-Q1
print(IQR)

data.describe()

print(data2)