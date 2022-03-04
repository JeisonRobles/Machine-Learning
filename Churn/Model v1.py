# -*- coding: utf-8 -*-
"""
#Testing

@author: Jeison Robles
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



Customer_Churn_DF = pd.read_csv("C:\Jeison\Python\CUSTOMER CHURN\Churn_Modelling.csv")


print(Customer_Churn_DF.isnull().sum())
print(Customer_Churn_DF.nunique())

Churn_DF = Customer_Churn_DF.drop(['RowNumber', 'CustomerId','Surname'], axis =1 )

# print(Churn_DF.shape)

#EXPLORATORY DATA ANALYSIS

#1 means you leave, 0 means you stay


# Labels = 'Retained','Exited'
# sizes = [Churn_DF.Exited[Churn_DF['Exited']==0].count() , Churn_DF.Exited[Churn_DF['Exited']==1].count()]
# explode = (0, 0.1)
# fig1, ax1 = plt.subplots(figsize=(10,8))
# ax1.pie(sizes,explode=explode, labels=Labels, autopct='%1.1f%%',startangle=90)
# plt.show()

# fig, axarr = plt.subplots(2,2, figsize=(20,12))
# sns.countplot(x="Gender", hue='Exited',data=Churn_DF, ax=axarr[0][0])
# sns.countplot(x='Geography', hue ='Exited', data=Churn_DF, ax= axarr[0][1])
# sns.countplot(x="HasCrCard", hue='Exited', data=Churn_DF, ax=axarr[1][0])
# sns.countplot(x='IsActiveMember', hue='Exited', data = Churn_DF, ax=axarr[1][1])



# fig, axarr = plt.subplots(3, 2, figsize=(10,12))

# sns.boxplot(y = 'CreditScore', x='Exited', hue='Exited', data=Churn_DF, ax = axarr[2][1])
# sns.boxplot(y = 'Age', x='Exited', hue='Exited', data=Churn_DF, ax = axarr[0][0])
# sns.boxplot(y = 'Tenure', x='Exited', hue='Exited', data=Churn_DF, ax = axarr[0][1])
# sns.boxplot(y = 'Balance', x='Exited', hue='Exited', data=Churn_DF, ax = axarr[1][0])
# sns.boxplot(y = 'NumOfProducts', x='Exited', hue='Exited', data=Churn_DF, ax = axarr[1][1])
# sns.boxplot(y = 'EstimatedSalary', x='Exited', hue='Exited', data=Churn_DF, ax = axarr[2][0])



Churn_DF_Train = Churn_DF.sample(frac=0.8,random_state=200)
# Churn_DF_Test = Churn_DF.sample(frac=0.2, random_state=200)
Churn_DF_Test = Churn_DF.drop(Churn_DF_Train.index)
print(len(Churn_DF_Test))
print(len(Churn_DF_Train))

Churn_DF_Train['BalanceSalaryRatio'] = Churn_DF_Train.Balance / Churn_DF_Train.EstimatedSalary
Churn_DF_Train['TenureByAge'] = Churn_DF_Train.Tenure / Churn_DF_Train.Age
Churn_DF_Train['CreditScoreGivenAge'] = Churn_DF_Train.CreditScore / Churn_DF_Train.Age

sns.boxplot(y='BalanceSalaryRatio', x= 'Exited', hue='Exited',data=Churn_DF_Train)
plt.ylim(-1,5)

sns.boxplot(y='TenureByAge', x='Exited', hue='Exited', data= Churn_DF_Train)

plt.ylim(-1, 2)

print(Churn_DF_Train.head())
print(Churn_DF_Train.nunique())



#DATA PREPARATION FOR MODEL FITTING

Numerical_Variables = ['CreditScore','Age','Tenure','Balance','NumOfProducts','EstimatedSalary','BalanceSalaryRatio','TenureByAge','CreditScoreGivenAge']
Categorical_Variables = ['HasCrCard','IsActiveMember','Geography','Gender']

Churn_DF_Train = Churn_DF_Train[['Exited'] + Numerical_Variables + Categorical_Variables]
print(Churn_DF_Train.head())


#We have to be carefull with the categorical values that has zero because mathmatical is incorrect to consider, so change ir to -1 that dont generate problems.

Churn_DF_Train.loc[Churn_DF_Train.HasCrCard ==0,'HasCrCard'] = -1
Churn_DF_Train.loc[Churn_DF_Train.IsActiveMember == 0, 'IsActiveMember'] =-1
print(Churn_DF_Train.head())


#One Hot Encodding

One_Hot_Column = pd.get_dummies(Churn_DF_Train.Geography)
Churn_DF_Train = Churn_DF_Train.drop('Geography', axis=1)
Churn_DF_Train = Churn_DF_Train.join(One_Hot_Column)

One_Hot_Column = pd.get_dummies(Churn_DF_Train.Gender)
Churn_DF_Train = Churn_DF_Train.drop('Gender', axis=1)
Churn_DF_Train = Churn_DF_Train.join(One_Hot_Column)

print(Churn_DF_Train.head())


#SCALLING by natural

min_Vector = Churn_DF_Train[Numerical_Variables].min().copy()
max_Vector = Churn_DF_Train[Numerical_Variables].max().copy()



Churn_DF_Train[Numerical_Variables] = (Churn_DF_Train[Numerical_Variables] - min_Vector)/(max_Vector - min_Vector)





from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

LR = LogisticRegression(random_state=0)
LR.fit(Churn_DF_Train.loc[:,Churn_DF_Train.columns !='Exited'],Churn_DF_Train.Exited)

print('LOGISTICAL REGRESSION CLASSIFICATION REPORT: \n',classification_report(Churn_DF_Train.Exited, LR.predict(Churn_DF_Train.loc[:,Churn_DF_Train.columns != 'Exited'])))

RF = RandomForestClassifier(max_depth=2, random_state=0)
RF.fit(Churn_DF_Train.loc[:,Churn_DF_Train.columns !='Exited'], Churn_DF_Train.Exited)

print('RANDOM FOREST CLASSIFICATION REPORT: \n', classification_report(Churn_DF_Train.Exited, RF.predict(Churn_DF_Train.loc[:,Churn_DF_Train.columns != 'Exited'])))


# PLOTTING RESULTS

plt.figure(figsize = (12,6), linewidth = 1)
plt.plot()



