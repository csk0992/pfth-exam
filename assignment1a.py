# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:35:11 2022

@author: fnatm
"""

'''
In order to ensure that my script can continue the pattern, I will write the code around a while loop. 
It needs to be able to increase the number of asterisks one by one continuously until there are 9 in a single line, 
and then decrease one by one until there is only 1 left, repeatedly. A two-variable design will be used, 
one for the number of asterisks and another to control the rate of increase and decrease. 

The sys module will be imported in order to envelop the while loop in a try statement, 
so that the sys.exit() function can be added with an except statement, declaring the ctrl+c command the necessary input with a keyboardInterrupt error. 
Also, the length variable is created to measure the time in which the script has run,
and is set to break the loop after 10 seconds as a default setting, but this can be
lengthened or shortened depending on what is required.

I want the code to be able to run continuously, but I do not want an unstoppable infinite loop, so I need to be able to stop it. 
Lastly, for ease of reading and running the code, the time module is added in order to enter a 0.1 second pause between every printed line via the time.sleep() function.
'''

import time, sys
asterisk = 1 # How many asterisks to print
asteriskIncreasing = True # Whether the number of * is increasing or not

start = time.time()

try:
    while asterisk <= 10: # The main program loop
        print('*' * asterisk)
        time.sleep(0.1) # Pause for 1/10th of a second
        
        if asteriskIncreasing:
            # Increase the number of *:
            asterisk = asterisk + 1
            if asterisk == 9:
                # Change direction:
                asteriskIncreasing = False
        
        else:
            # Decrease the number of *:
            asterisk = asterisk - 1
            if asterisk == 1:
                # Change direction:
                asteriskIncreasing = True
        
        end = time.time()
        length = end - start
        if length >= 10:
            break
            
except KeyboardInterrupt:
    sys.exit()
