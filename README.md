# Assignment 1
## Pattern Generation 
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction 
Write a script that uses flow control statements to generate the following pattern. Ensure that your script can continue the pattern.
```sh
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
```

- One type of data, asterisks

- Repeating lines

- Only change is number of asterisks

- Increases and decreases in increments of 1

- minimum 1 asterisk, maximum of 9

## Outcome
- Considerations regarding methods are written in `assignment1a.py`, which also contains the code to solve this task.
## Discussion
Worked with no issues. Other types of loops could have been used, but since no length of continuation was specified, an infinite loop with an opt-out error condition was deemed more effective. A break statement would’ve been dependent on the code and not the user, and a for loop would only have continued the code a finite number of times.

