# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 02:36:57 2022

@author: fnatm
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
The full given dataset is read into a dataframe first,
after which it is used to pluck out rows corresponding
to two regions, Western Europe and Sub-Saharan Africa.
The two regions are plotted into new and separate dataframes,
which are then put in a list to be put together into a
new dataframe with only the two regions together.
pd.concat() is used for this purpose since both filtered
dataframes use the same columns, and can simply be concatenated
into a single dataframe.
'''

df = pd.read_csv('figures/data/world-happiness-report-2021.dat', usecols = ['Regional indicator', 'Ladder score', 'Logged GDP per capita', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'])
            
df_filtered1 = df[df['Regional indicator'] == 'Western Europe'] 
df_filtered2 = df[df['Regional indicator'] == 'Sub-Saharan Africa']

regions = [df_filtered1, df_filtered2]

dataset = pd.concat(regions)

'''
The 7 columns that the pairplot needs to take into account 
are then put into a variable, and the title, size, and
empty space of the pairplot is then taken into account.
Most importantly, the hue variable in the pairplot function 
itself is set to be dependent on the Regional Indicator
column, so that the two filtered out regions will be
represented with different colors in the final visualization.
This also allows the reg parameter to add a regression line
for both regions within each plot. Lastly the pairplot is saved and closed.
'''

dataset_7attrib = dataset[['Regional indicator','Ladder score','Logged GDP per capita',
             'Healthy life expectancy','Freedom to make life choices','Generosity',
             'Perceptions of corruption']]
ax1 = plt.figure(dpi = 300)
sns.pairplot(dataset_7attrib, hue = 'Regional indicator', kind = 'reg', plot_kws={'line_kws':{'color':'red'}})
plt.title("Pairplot of Happiness Attributes",size=15)
plt.tight_layout()
plt.savefig('attributes_happy.png')
plt.close()
