import pandas as pd
from collections import Counter
df = pd.read_csv("horoscopes.csv")

'''
Given difference function from the source code evaluates two lists into
separate sets and creates a list based on which words in the first list are not
present in the second one. With that in mind, it is changed to compare 
a given list with a higher number of other lists, since I am working with 
three horoscopes.
'''

def difference(lst1, lst2, lst3):
    return list(set(lst1).difference(set(lst2)).difference(set(lst3)))

'Extract specific rows and cells corresponding to specific horoscopes.'
idxsV = df['sign'] == 'virgo'
textsV = df['horoscope-clean'].loc[idxsV].values

"""
Turn the .csv data into individual words. There's no need for 
the big stopword + tokenizer red carpet from assignment2a to roll out, 
since I am interested in words that the signs do not have in common. 
In that case, splitting the items in the text and using extend() 
to add them to an empty list will do the trick.
"""

wordsV = []
for item in textsV:
    wordsV.extend(item.split())

'Add to Counter object, find top 200.'

v200 = []

vCounter = Counter(wordsV)

'Counter holds a list of tuples with value + number of appearances in original .csv, we only need the top 200 values:'
for k, v in vCounter.most_common(200):
    v200.append(k)


'Repeat for Taurus.'
idxsT = df['sign'] == 'taurus'
textsT = df['horoscope-clean'].loc[idxsT].values

wordsT = []
for item in textsT:
    wordsT.extend(item.split())

t200 = []

tCounter = Counter(wordsT)

for k, v in tCounter.most_common(200):
    t200.append(k)


'Repeat for Pisces.'    
idxsP = df['sign'] == 'pisces'
textsP = df['horoscope-clean'].loc[idxsP].values

wordsP = []
for item in textsP:
    wordsP.extend(item.split())

p200 = []

pCounter = Counter(wordsP)

for k, v in pCounter.most_common(200):
    p200.append(k)

'Use the difference function to print out what words are in the first list but not in the other 2 for each.'
diffV_TP = difference(v200, t200, p200)

diffT_PV = difference(t200, p200, v200)

diffP_VT = difference(p200, v200, t200)


print('Words in top 200 for Virgo not present in Taurus and Pisces:')
print(diffV_TP)

print('Words in top 200 for Taurus not present in Pisces and Virgo:')
print(diffT_PV)

print('Words in top 200 for Pisces not present in Virgo and Taurus:')
print(diffP_VT)

