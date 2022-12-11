# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:27:01 2022

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

'''
As with the first task of the assignment, dataset
is read into a frame and then indexed to pick out
two horoscopes.
'''

data = pd.read_csv('horoscopes.csv')   

idxs0 = data['sign'] == 'aries'
idxs1 = data['sign'] == 'taurus'
idxs = idxs0.values + idxs1.values

'''
Corpus is extracted and vectorized using word count again,
and so is the model data, again with an 80/20 split.
'''

corpus = data['horoscope'].loc[idxs].values
cv = CountVectorizer()

x = cv.fit_transform(corpus).toarray()
y = data['sign'].loc[idxs].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20)

'''
Classifier is called on the training data,
and a confusion matrix is computed and
saved to a visualization with the same
settings.
'''

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
plt.savefig('figures/horo2cmNoPrep.png')
plt.close()

'''
Relative and absolute classification accuracy are computed
and printed, followed up by a tenfold cross validation,
which is then saved as a histogram.
'''

print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
print(f'Accuracy in instances {accuracy_score(y_test, y_pred, normalize=False)}')

accuracies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10)    
print(accuracies.mean())
print(accuracies.std())

plt.hist(accuracies, density=True, bins=30)  
plt.xlabel('Accuracy')
plt.ylabel('Probability')
plt.savefig('figures/horoNoPrep.png')
plt.close()

''' An extra line in case I want to run both binary
configurations at once for the sake of a direct
comparison between the printed data.

exec(open('assignment5b_prep.py').read())
'''