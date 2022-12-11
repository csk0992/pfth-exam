# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:36:27 2022

@author: fnatm
"""

'''
A while loop with a break statement for the correct password should accomplish the given task. 
The while loop will print statements like asking for the user’s name, 
politely asking them to type the password and even giving hints. 
The str() function is used to incorporate the user’s name into the printed messages together with the input() function, 
which is also used to receive their guesses at the password, 
and an if and an elif statement are used to check if the password, 
‘nightingale’, has been typed correctly or not.
'''

while True:
    print('Hello. What is your name?')
    name = input()
    print('Hello, ' + str(name) + '.')
    while True:
        print('Please type the password. Hint, it is a bird. Also, type "go back" if you wish to change your name.')
        global password
        password = input()
        if password == 'go back':
            break
        elif password != 'nightingale':
            print('Wrong password.')
        elif password == 'nightingale':
            break
    if password == 'nightingale':
        break
print('Access granted.')
