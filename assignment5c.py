# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 00:40:38 2022

@author: fnatm
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

data = pd.read_csv('horoscopes.csv')   

corpus = data['horoscope-clean'].values
cv = CountVectorizer()

X = cv.fit_transform(corpus).toarray()
y = data['horoscope-clean'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)

classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
classifier.fit(X_train , y_train)

y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)

print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
print(f'Accuracy in instances {accuracy_score(y_test, y_pred, normalize=False)}')

accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)    
print(accuracies.mean())
print(accuracies.std()) 

plt.hist(accuracies, density=True, bins=30)
plt.xlabel('Accuracy')
plt.ylabel('Probability')

plt.savefig('figures/horoscopesAll.png')
plt.close()