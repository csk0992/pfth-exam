# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 01:54:51 2022

@author: fnatm
"""

'''
Dataset is loaded into a dataframe and the needed 8 rows are pulled out of it
in separate series. On top of that, a list is created covering the 40 days the
dataset spans, to serve as the x-axis of the plots created.

Each of the 8 series are passed to a variable to be inserted into separate plots
under the subplots() function, all with the timetable list as the x-axis.
A label is then added for each to be passed to the legend() function so the
final plot has a guide to the labels.

Lastly the plot is saved and closed, leaving me with 8 lines for 8 patients in
a single graph.
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('figures/data/series-05.csv')    
line1 = df.iloc[0]
line2 = df.iloc[1]
line3 = df.iloc[2]
line4 = df.iloc[3]
line5 = df.iloc[4]
line6 = df.iloc[5]
line7 = df.iloc[6]
line8 = df.iloc[7]
inflaPeriod = list(range(1,41))
    
fig, ax = plt.subplots()
ax.plot(inflaPeriod, line1, label='pat1')
ax.plot(inflaPeriod, line2, label='pat2')
ax.plot(inflaPeriod, line3, label='pat3')
ax.plot(inflaPeriod, line4, label='pat4')
ax.plot(inflaPeriod, line5, label='pat5')
ax.plot(inflaPeriod, line6, label='pat6')
ax.plot(inflaPeriod, line7, label='pat7')
ax.plot(inflaPeriod, line8, label='pat8')
plt.xlabel('40 Day Period')
plt.ylabel('Infl. rate')
ax.legend()
    
plt.savefig('assignmentVisualStacked.png')
plt.close()

'''
Now we need the same 8 lines split apart in separate graphs. The subplots
receive a title and are arranged into 4 columns of 2 for simplicity's sake.
Next up, the 8 series representing the patients are plotted into separate axs[]
and given proper individual labels.

Lastly, labels are set on each x- and y-axis for the sake of clarity, but to
not clutter the subplots too much, all labels not along the outer rim of the
subplots are removed, as the axises run on the same parameters. The finishing
touch is the tight_layout() function being called to manage the space between
graphs, then the separated graphs can be saved in a png and closed.
'''

fig, axs = plt.subplots(2, 4)
fig.suptitle('Separately Stacked Patients')
axs[0, 0].plot(inflaPeriod, line1)
axs[0, 0].set_title('Patient 1')
axs[1, 0].plot(inflaPeriod, line2)
axs[1, 0].set_title('Patient 2')
axs[0, 1].plot(inflaPeriod, line3)
axs[0, 1].set_title('Patient 3')
axs[1, 1].plot(inflaPeriod, line4)
axs[1, 1].set_title('Patient 4')
axs[0, 2].plot(inflaPeriod, line5)
axs[0, 2].set_title('Patient 5')
axs[1, 2].plot(inflaPeriod, line6)
axs[1, 2].set_title('Patient 6')
axs[0, 3].plot(inflaPeriod, line7)
axs[0, 3].set_title('Patient 7')
axs[1, 3].plot(inflaPeriod, line8)
axs[1, 3].set_title('Patient 8')

for ax in axs.flat:
    ax.set(xlabel='40 Day Period', ylabel='Infl. rate')
    
for ax in axs.flat:
    ax.label_outer()

fig.tight_layout()
plt.savefig('assignmentVisualSeparate.png')
plt.close()

'''
Two major factors stand out to me regarding the advantages of stacked vs separate plots: comparison and scrutiny.
Stacked plots seem significantly easier to compare directly, it would require time and focus to draw comparisons between separated plots. 

Granted, a larger number of plots entered into the same graph will naturally turn into a mess of colors and lines quickly, 
so on some occasions separated plots will be ideal regarding this aspect. You would just need to take into account that if, say, 
you’re presenting the visualizations in a PowerPoint, that the separated plots need extra time on screen, clear captions, 
and/or a very concise explanation to ensure your audience is following along. On top of that, 
separated plots within the same visualization will naturally result in smaller graphs, 
so your audience’s ability to take in the information of each graph will naturally take longer and require more of a guiding hand. 

Stacking 8 lines of different colors into one graph can be overwhelming too, even with a legend added to the plot, 
but perhaps by adding points to certain stand-out line points to emphasize them, adding captions, 
or taking advantage of the larger singular graph to physically point out interesting spikes on higher or lower ends, 
which would naturally stand out above the other lines on the graph.
'''