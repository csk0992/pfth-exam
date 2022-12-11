# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:51:23 2022

@author: fnatm
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay as cmd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

data = pd.read_csv('horoscopes.csv')    

idxs0 = data['sign'] == 'aries'
idxs1 = data['sign'] == 'taurus'
idxs = idxs0.values + idxs1.values

'''
Other than the filenames for the visualizations, 
the only difference between assignment5b.py and
this script is the parameters used in the CountVectorizer()
function, so the same documentation comments apply here.

The parameters added makes the script ignore terms
with a document frequency above 0.9 and below 0.5, 
(integers are just the standard for minimum document frequency) 
and takes scikitlearn's english stopword list into
account, in order to highlight the effects of preprocessing.
'''

corpus = data['horoscope'].loc[idxs].values
cv = CountVectorizer(max_df=0.9, min_df=5, stop_words='english')

x = cv.fit_transform(corpus).toarray()
y = data['sign'].loc[idxs].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20)

classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)

color = 'black'
matrix = cmd.from_predictions(y_test, y_pred, cmap=plt.cm.Blues)
matrix.ax_.set_title('Confusion Matrix', color=color)
plt.xlabel('Predicted Label', color=color)
plt.ylabel('True Label', color=color)
plt.gcf().axes[0].tick_params(colors=color)
plt.gcf().axes[1].tick_params(colors=color)
plt.savefig('figures/horo2cmPrep.png')
plt.close()

print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
print(f'Accuracy in instances {accuracy_score(y_test, y_pred, normalize=False)}')

accuracies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10)    
print(accuracies.mean())
print(accuracies.std())

plt.hist(accuracies, density=True, bins=30)  
plt.xlabel('Accuracy')
plt.ylabel('Probability')
plt.savefig('figures/horoPrep.png')
plt.close()