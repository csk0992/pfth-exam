# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:32:13 2022

@author: fnatm
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay as cmd
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

'''Horoscope data gets read into a dataframe and indexed
to pick out text data for two chosen horoscopes. Also renders
deduplication unnecessary as no two horoscopes, at least
within a timeframe like this one's, are the exact same text.'
'''
data = pd.read_csv('horoscopes.csv')

idxs0 = data['sign'] == 'virgo'
idxs1 = data['sign'] == 'leo'
idxs = idxs0.values + idxs1.values

'''
Corpus of texts is extracted and vectorized with raw word counts.
Following up model data is extracted as well and split 80/20 for
training and testing.
'''

corpus = data['horoscope'].loc[idxs].values
cv = CountVectorizer()

x = cv.fit_transform(corpus).toarray()
y = data['sign'].loc[idxs].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.20)

'''
Instantiating the NB classifier to call it with the training data percentage.
A confusion matrix is then computed and added to the printed output.
'''

classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)

'''
Confusion matrix is then entered into a plot with the colors edited for easy
visibility, which is then saved and closed.
'''

color = 'black'
matrix = cmd.from_predictions(y_test, y_pred, cmap=plt.cm.Blues)
matrix.ax_.set_title('Confusion Matrix', color=color)
plt.xlabel('Predicted Label', color=color)
plt.ylabel('True Label', color=color)
plt.gcf().axes[0].tick_params(colors=color)
plt.gcf().axes[1].tick_params(colors=color)
plt.savefig('figures/horo1cm.png')
plt.close()

'''
Next up, relative and absolute classification accuracy is computed,
to summarize the classification model's performance.
'''

print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
print(f'Accuracy in instances {accuracy_score(y_test, y_pred, normalize=False)}')

'''
Finally, tenfold cross validation is run, and the distribution
of accuracy is saved as a histogram.
'''

accuracies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10)    
print(accuracies.mean())
print(accuracies.std())

plt.hist(accuracies, density=True, bins=30)  # density=False would make counts
plt.xlabel('Accuracy')
plt.ylabel('Probability')
plt.savefig('figures/horoAccDist.png')
plt.close()