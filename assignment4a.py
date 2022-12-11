# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:12:45 2022

@author: fnatm
"""

'''
The function requires two variables, one for the filename of the source of 
data, and one for the name of the file that the series visualization is saved 
as. I'm working with csv files and thus setting the delimiter accordingly, 
after which the filename variable along with it is loaded into a numpy array
to pass to a linear plot, which is then saved and closed. Lastly an example of
the function in use is added.
'''
import numpy as np
import matplotlib.pyplot as plt

def makeVis(a, b):
    data = np.loadtxt(fname=a, delimiter=',')
    plt.imshow(data)
    plt.savefig(b)
    plt.close()
    
makeVis('figures/data/series-04.csv', 'figures/assignmentVisual.png')
    