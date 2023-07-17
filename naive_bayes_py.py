# -*- coding: utf-8 -*-
"""Naive_Bayes.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_3zZeusDOuqHiXSUl90C8hbVuac8n7lX
"""

# Import libraries

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Read CSV files
train_df = pd.read_csv('/content/Train.csv')

# Convert the first row to the columns' names
train_df.columns = train_df.iloc[0]

# Delete the first row as it represents the names of columns
train_df = train_df.drop([0])

# Delete the Patient number as it useless
train_df = train_df.drop(['Pat .N. '], axis=1)

train_df.head(15)

# Read CSV files
test_df = pd.read_csv('/content/Test.csv')

# Convert the first row to the columns' names
test_df.columns = test_df.iloc[0]

# Delete the first row as it represents the names of columns
test_df = test_df.drop([0])

# Delete the Patient number as it useless
test_df = test_df.drop(['Pat .N. '], axis=1)

test_df.head()

# A pre-processing function to delete spaces and qoutes
def normalize(text):
  text = text.replace(' ', '')
  text = text.replace('"', '')
  text = text.replace('“', '')
  text = text.replace('”', '')
  return text

# Apply 'normalize' function on the data
for col in train_df.columns:
  train_df[col] = train_df[col].apply(normalize)

train_df.head(15)

# Apply 'normalize' function on the data
for col in test_df.columns:
  test_df[col] = test_df[col].apply(normalize)

test_df.head()

# Check the values that exist in each column
for col in train_df.columns:
  print(col, train_df[col].unique())

# Check the values that exist in each column
for col in test_df.columns:
  print(col, train_df[col].unique())

# Apply label encoding on training and test data
le = LabelEncoder()

for col in train_df.columns:
  if len(train_df[col].unique()) == 2:
    train_df[col] = le.fit_transform(train_df[col])
    test_df[col] = le.transform(test_df[col])

train_df.head(15)

test_df.head()

# Apply label encoding on training and test data
# There are many ways to apply the OneHot Encoding. Here we used pandas library to do it
cols = []

for col in train_df.columns:
  if len(train_df[col].unique()) > 2:
    cols.append(col)

train_df = pd.get_dummies(train_df, columns = cols)

test_df = pd.get_dummies(test_df, columns = cols)
test_df = test_df.reindex(columns = train_df.columns, fill_value=0)

train_df.head()

test_df.head()

"""# Naive Bayes is a classification technique that is based on Bayes’ Theorem with an assumption that all the features that predicts the target value are independent of each other."""

# Import all types of Naive Bayes algorithm that implemented in sicket learn
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB

# Split train and test data to X and Y (features and label)
X_train = train_df.loc[:, train_df.columns != 'Coronary Dis .']
X_test = test_df.loc[:, train_df.columns != 'Coronary Dis .']
y_train = train_df['Coronary Dis .']
y_test = test_df['Coronary Dis .']

#Create a Gaussian Classifier
model = GaussianNB()

#Train the model using training set
model.fit(X_train, y_train)

#Test the model using test set
predicted = model.predict(X_test)

print('Accuracy on train set:' , model.score(X_train, y_train))
print('Accuracy on test set:' , model.score(X_test, y_test))

#Create a MultinomialNB Classifier
model = MultinomialNB()

#Train the model using training set
model.fit(X_train, y_train)

#Test the model using test set
predicted = model.predict(X_test)

print('Accuracy on train set:' , model.score(X_train, y_train))
print('Accuracy on test set:' , model.score(X_test, y_test))

#Create a ComplementNB Classifier
model = ComplementNB()

#Train the model using training set
model.fit(X_train, y_train)

#Test the model using test set
predicted = model.predict(X_test)

print('Accuracy on train set:' , model.score(X_train, y_train))
print('Accuracy on test set:' , model.score(X_test, y_test))

#Create a BernoulliNB Classifier
model = BernoulliNB()

#Train the model using training set
model.fit(X_train, y_train)

#Test the model using test set
predicted = model.predict(X_test)

print('Accuracy on train set:' , model.score(X_train, y_train))
print('Accuracy on test set:' , model.score(X_test, y_test))

#Create a CategoricalNB Classifier
model = CategoricalNB()

#Train the model using training set
model.fit(X_train, y_train)

#Test the model using test set
predicted = model.predict(X_test)

print('Accuracy on train set:' , model.score(X_train, y_train))
print('Accuracy on test set:' , model.score(X_test, y_test))