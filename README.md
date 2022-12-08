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

### Outcome
- Considerations regarding methods are written in `assignment1a.py`, which also contains the code to solve this task.
### Discussion
Worked with no issues. Other types of loops could have been used, but since no length of continuation was specified, a while loop with opt-out conditions was deemed more effective. A `break` statement and a `KeyboardInterrupt` option means the script has both user-dependent and code-dependent end conditions.

## Authorization Test
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction 
Write a script that uses at least one function to accept user input of name and password, prints a polite welcome to the user, and tests if the password is correct (you decide the correct password).

Task requirements:

- use at least one function

- accept user input of their name

- accept user input of their password

- print a polite welcome

- test if password decided by me is correct

### Outcome
- Considerations regarding methods are written in `assignment1b.py`, which also contains the code to solve this task.
### Discussion
Task successful. However, during writing, the code jumping back and starting all over in a single loop became a clumsy and undesirable aspect of the code, so effort was taken to change this. An additional while loop was added inside the existing one, but after all code related to the name variable. The new code asks for user input for the variable password, using if and elif statements while taking order of execution into account to allow the user to either guess the password wrong, guess the password correctly, or type “go back” if they wish to change their name, making the act of starting the code all over a voluntary affair instead. The print statement at the beginning of the loop is adjusted to mention this third option. For the sake of simplicity in writing, both typing the password correctly and typing “go back” are set to execute break statements, but in return the password variable is given the keyword global, and as it calls the original loop, an if statement checks the variable again. Has the password been typed correctly, the first while loop in the call stack triggers another break statement to print out “Access granted.” Has the second while loop broken because of the break statement for typing “go back”, then the first while loop’s break statement is not executed, and instead the user is allowed back to the top of the code, to change their name.

# Assignment 2
## With Or Without Function Words
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction 
Compare the top 100 most frequent words in all horoscopes with and without stopwords (i.e. function words), what seems to be the most striking differences? You should include your stopword list (or a link to) in the answer.

- 1 type of data, string values from a .csv file

- needs to be sorted:

- only a specific column is required

- and only top 100 most frequent words from said column

- 2 separate objects are required, the top 100 with stopwords and without stopwords

- objects must be converted to a string format recognizable to the wordcloud module while still recognizing each word as separate

### Outcome
- Considerations regarding methods are written in `assignment2a.py`, which also contains the code to solve this task.
### Discussion
![image](https://user-images.githubusercontent.com/120116455/206515615-8b74836b-b6be-461d-b5d9-0bdf7655ed39.png)

This image includes stopwords.

![image](https://user-images.githubusercontent.com/120116455/206515769-4333337d-096a-44ec-8f05-fb621673bae3.png)

This image has filtered away the stopwords.

Worked as intended. The wordcloud without stopwords is notably more clear and highlights non-function words that can lead to potential analysis. However, I would note that the words in question are very general, and that if one desired more specific information from this method, it could be beneficial to run this code several times, manually extending the stopword list with the common neutral words still present, like “today” and “people.”

## Sign-specific indexing
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction 
Compare the top 200 most frequent words for at least three different Zodiac signs (ex. virgo, leo, pisces) using the `difference` set function from Problem 1. Are there any apparent characteristics/distinct differences between the signs?

- 1 type of data, string values from a .csv file

- needs to be sorted:

  - cells from a specific column are required

  - corresponding to specific rows

  - and only top 200 most frequent words from each row category

- difference set function needs to be readjusted to apply to the task

### Outcome
- Considerations regarding methods are written in `assignment2b.py`, which also contains the code to solve this task.
### Discussion
Code output is:
```
Words in top 200 for Virgo not present in Taurus and Pisces:
['effort', 'less', 'never', 'everything', 'also', 'off', 'matters', 'year']

Words in top 200 for Taurus not present in Pisces and Virgo:
['But', 'warn', 'bad', 'both', 'Taurus', 'positive', 'point', 'makes', 'energy', 'far']

Words in top 200 for Pisces not present in Virgo and Taurus:
['through', 'ways', 'nothing', 're', 'Pisces', 'away', 'little', 'changes', 'act', 'every', 'planet', 'why', 'which', 'full']`
```
If I were to pick out one word that seems the most charged with meaning for each list, it would be “effort”, “warn”, and “act”.

I think I would personally have desired a larger data output if I were to attempt to validate the answers I got, so perhaps horoscopes from a greater time period would be ideal.

Either way a set of lists like these don’t particularly indicate very strong differences between horoscopes, and while that does coincide with my personal expectations of horoscopes, I would still say the ideal way forward from here would be validations of the data, whether via expanding the original text resource, or via picking out sample appearances of these words and reading the context of the full cell value, since the majority of them can enter multiple meanings depending on the sentence they exist in. For example, “act” being a common word for Pisces imply horoscopes describing some sort of active event, but whether a call to action or a warning against rash decisions is not something I can tell from these lists alone.

They do however tell me where to search for further meaning, so I would still deem this task successful.

# Assignment 3
## A Registry for Adventure Scout League participants (NB: the following body of text is intended to answer all three tasks at the same time.)
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 

I want to create a script that can summarize important attributes about teams participating in the Adventurespejdliga, do the same for the challenges you can participate in during a typical season of the league, and finally check whether or not a given team is eligible for participation in a given challenge, as they have very different criteria, and while it is ideal for all teams to do all challenges if they wish to win the league, it is not required to participate.

I need two classes of objects to make this possible, one for teams and one for challenges. 
I’ll use a flat and simple level of abstraction, since it is intended purely for internal upkeep by staff, and first-hand experience tells me that for example the location of a challenge and the name of a scouting group is more than enough to gain a geographical overview.

The biggest potential opportunity to create any child classes that stood out was to potentially make an oldboys subclass that inherits the attributes of the team class and adds an attribute that takes into account that team member ages require them to participate in secondary competition categories within a challenge.

However, given that the age range of the primary and secondary categories are decided by each individual challenge, and that some of them do not even have a secondary category, it was deemed much simpler and more streamlined to instead cover this aspect of the design with list type attributes in the challenge class, and simply make sure my eligibility comparison function takes those into account when presenting the final result.

![image](https://user-images.githubusercontent.com/120116455/206521649-f50f0048-b300-4f6d-8069-a709bf288311.png)

Objects in the team class are passed five attributes:

- the team’s name 

- the number of people in it 

- which scouting group they’re based out of 

- the age of the oldest team member 

- and the age of the youngest

Objects in the challenge class are also passed five attributes: 

- the challenge’s name 

- the interval of eligible team sizes to participate 

- the interval of eligible ages that the whole team needs to fit within to participate in the primary category 

- and if the challenge has a secondary category then also the age range interval for that one, otherwise an empty list  (only one team member needs to be within it for the team to be passed to said category, the rest could be young enough for the primary category and it would still be the case)

- and finally the given location for the challenge’s starting point, taking into account that the last attribute may intentionally be kept secret from the official website https://adventurespejd.dk/loeb where my data comes from, so some challenges cannot have their location added yet.

The team class is also given the `getTeam()` method in order to present the attributes of a given team in a string for quick and clear summarization, and the challenge class’s `getChal()` has the same function for its class. It is worth adding that while `getTeam()` should be able to accurately sum up a team object with one printed phrasing, the potential lack of secondary category, known location, or both attributes mean that `getChal()` needs to prepare 4 phrasings for print depending on the object used in the method call.

Finally, to take full advantage of the created classes and using their objects to carry out my desired function, `checkEligible()` is added as a function calling both a team object and a challenge object to compare their attributes:

- team name and challenge name are used to know which objects you’re comparing

- team size is used to check if it falls within the eligible challenge interval for number of participants

- Since any potential secondary category won’t have an upper age limit, highest age in the team object only needs to be used to check whether the team falls within said category in the first place, if it even exists in the challenge object. No need to worry whether the team object falls completely out of said category

- On the other hand, primary categories have a more limited interval of age, so the function also checks whether the team object’s lowest age falls below that interval, in which case the team is fully ineligible to participate.

- again, scoutGroup and chalLocat are relevant attributes for the targeted users of this script, but there is no need to compare them directly in a function. That would require an entirely separate block of code, and it would not add relevant information.

The full script is in the `assignment3.py` file. It includes the classes written out in code along with further explanations, as well as an example instantiating the classes by putting example objects within the `main()` function.

Were I to keep elaborating on this project, future expansions on the script could include relating it to actual registration by for example taking the maximum number of teams for a challenge into account, or adding a scorekeeping system across a given season.

# Assignment 4

