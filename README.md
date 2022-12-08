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
## Custom Plotting Function
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction
Write a function that can take a (time) series and a filename as input and generates a series visualization that is stored under the filename.

To solve this task in relation to the given .csv files with patient data, my function needs to include the following:

- two variables corresponding to the name of the series and the filename to save it under
- the ability to load a given series into a numpy array
- passing the array to a plot to create the series visualization
- saving the plot with the second variable as filename, and closing it

### Outcome
These considerations have been implemented into the attached `assignment4a.py` file, along with instantiating the function at last to show it in use. The following plot is the output.

![assignmentVisual](https://user-images.githubusercontent.com/120116455/206572465-3d1cedc9-3c02-42b0-9d78-e54e1b9bf2ea.png)

## To Stack Or Not To Stack
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction
In this problem you have to make two plots from at least eight series objects (rows) in one data file, e.g., series-01.csv. In the first plot, you have to stack the eight series in one plot, that is, they shold all be in the same plot window (i.e., stacked on top of each other). In the second plot, each series object should have its own subplot (i.e., a total of eight 'unstacked' subplots). Discuss the advantage/disadvantage of stacked vs unstacked plotting of series data.

To solve this task, my code needs to do the following:

- read a csv file into a dataframe and pick apart the first 8 rows in the file into separate series

- add a separate list to represent the time period for the dataset, which can serve as the x-axis for all subsequent plots in the script

- create a figure in which all 8 series subplots are visualized in the same ax object

- save it and close it

- create another figure in which the 8 series are visualized on separate ax objects

- save it and close it

### Outcome
For simplicity and ease of viewing, the plots used to visualize this task will be line graphs instead. The stacked plot will also have all 8 lines labeled and the `plt.legend()` function used to create an overview, and titles will be set for each object in the array of separated subplots. Labels will be added to the y- and x-axis of both the stacked and the separated plots, but the separated plots will only visualize the axis labels on the outer rim of the figure while also managing the space between plots using `fig.tight_layout().`

These considerations have been implemented in the attached script `assignment4c.py`, and the results are as follows:

Separate:

![assignmentVisualSeparate](https://user-images.githubusercontent.com/120116455/206573389-9a7a29cf-4f75-4b52-b2b3-70f943b81d31.png)

Stacked:

![assignmentVisualStacked](https://user-images.githubusercontent.com/120116455/206573433-6042a213-ee70-4dad-9370-02dcb8b9d540.png)

### Discussion
See the assignment file.

## Pairplot of World Happiness Survey
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction
Read the following columns from world-happiness-report-2021.dat here into a pandas dataframe:

- Regional indicator

- Ladder score

- Logged GDP per capita

- Healthy life expectancy

- Freedom to make life choices

- Generosity

- Perceptions of corruption

Extract the data for two regions using the Regional indicator column from the dataframe and create a pairplot using seaborn that compares the two regions. 

To accomplish this, my code needs to do the following:

- read specific columns from the given data into a pandas dataframe

- filter the data so I end up with only the rows within those columns that correspond to two given values in the Regional indicator column, as those designate the region the data in each row comes from

- create a pairplot that takes the filtered data and compares the two chosen regions across the other six attributes

The attached `assignment4d.py` show these criteria implemented. Pairplot layout and visual clarity were also taken into account by adjusting size, titles, color, and space between subplots. This was the result:

![attributes_happy](https://user-images.githubusercontent.com/120116455/206577424-40ff98ab-9fbf-44d9-94bd-e9a8afbdb637.png)

# Assignment 5
## Binary Classification
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction
Train a binary (two-label) Naive Bayes classifier that predicts two classes (e.g., virgo and pisces) of the sign variable from the horoscope content of horoscope. Knowing that the baseline (Zero Rate) accuracy is approximately 50%, discuss the performance (accuracy and confusion matrix) of your classifier.

In your submission, please discuss what your results mean for the genre of horoscopes (what can we learn about horoscopes from the study).

My script requires the following to accomplish the task:

- two horoscopes’ worth of clean text data extracted from the dataset

- corpus of text vectorized using raw word counts

- model data extracted from there to be split into training and testing data

- Naive Bayes classifier trained on the training data

- Confusion matrix computed and presented

- Classification accuracy computed

- x-fold cross validation ran on the model data and accuracy distribution presented in a plot for visualization 

### Outcome
- Considerations regarding methods are written in `assignment5a.py`, which also contains the code to solve this task.
### Discussion
A plot for the confusion matrix was added for the sake of additional visual clarity:
![horo1cm](https://user-images.githubusercontent.com/120116455/206581217-d714fa33-e61c-46fc-8f00-a32ba5c69746.png)

Additionally, cross validation was chosen to be done tenfold, and the following histogram was created from executing the script and saving the accuracy distribution of the cross validation:
![horoAccDist](https://user-images.githubusercontent.com/120116455/206581240-7a72a938-6160-48ec-aa59-9080fa082dca.png)

The multinomial NB algorithm predicts the tag for a piece of text based on highest probability out of all tags in a given sample. This makes it ideal for Natural Language Processing tasks but also gives it a definitive margin of error. Given that my script uses a binary classifier, the baseline accuracy for the two possible tags would be 50/50, truly impartially random chance. The script’s output confusion matrix and relative accuracy being so close to 50% implies a level of arbitrariness and lack of direct correlation that suits my colloquial understanding of written horoscopes.

## Effects of preprocessing
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
- Group submission: no
- Group members: none 
### Introduction
Preprocessing your natural language data before training a classifier can improve performance considerably. Look at the documentation for the `CountVectorizer()` function and use some of the parameters to preprocess your horoscope data. Then train two binary classifiers and discuss one with and one without preprocessing and compare the performance.

To solve this task, my script requires the following:

- all the same parameters as described for the Binary Processing task

- except done twice, and on the second time around the CountVectorizer() function must be based not on raw word count, but instead on altered parameters to preprocess data

- the ability to compare the preprocessed and non-preprocessed outputs

### Outcome
- Considerations regarding methods are written in `assignment5b.py` and `assignment5b_prep.py`, which also contain the code to solve this task.
### Discussion
Executing 5b, the script with no preprocessing, resulted in these plots:

![horo2cmNoPrep](https://user-images.githubusercontent.com/120116455/206582444-10679000-8aea-4a2b-865d-174f6cd42910.png)

![horoNoPrep](https://user-images.githubusercontent.com/120116455/206582469-d02c52cb-ea1d-499f-848f-7154299bed14.png)

A slightly higher accuracy can be viewed in both plots, but this is still a script based on the same dataset as task 1, and there is no immediate pattern to be found here either.

As for the script attached as `assignment5b_prep.py`, the `CountVectorizer()` function was altered to ignore document terms with a frequency above 0.9 and below 0.5, as well as to filter the corpus based on scikitlearn’s list of english stopwords, with the intention of concentrating the multinomial NB algorithm’s area of focus.

This resulted in the following plots:

![horo2cmPrep](https://user-images.githubusercontent.com/120116455/206582586-cd1e8747-2b84-4bef-8cfd-c7301456abd6.png)

![horoPrep](https://user-images.githubusercontent.com/120116455/206582607-e686a86e-4957-43c4-961e-92cd3f0560fd.png)

These visualizations leave the same impression of arbitrariness as the prior ones, and to emphasize that, they’re even showing a slightly lower accuracy than the script written exactly the same except with no preprocessing.

Since both scripts are written to print out multiple statements relating to the process of using the NB classifier, an optional extra line of code has also been added to the end of `assignment5b.py`, turned off by triple digits, that would open and execute `assignment5b_prep.py` if the digits are removed, for the sake of having the text output side by side for easier comparison.

Here are a few screenshots of this combined text output from different instances of executing the script:

![image](https://user-images.githubusercontent.com/120116455/206583286-611d5023-c1dc-434f-8484-319a48e41ddd.png)

The task description mentions how preprocessing your text data is meant to significantly improve performance, and I do follow the theory behind it as mentioned, that concentrating the corpus that you train and test your algorithm on to the most central and meaningful terms would increase its ability to predict the distribution of said terms.
With that in mind, I am inclined to believe that repeat instances of executing the two scripts show no correlation between accuracy and performance, and preprocessing, is a consequence of the arbitrary nature of written horoscopes, as discussed in task 1. There is no clear link between which script has the higher relative accuracy and which script’s 1-fold to 10-fold accuracy is highest either, and every instance only results in an accuracy slightly higher than the expected Zero Rate for this binary classifier. 
Repeating this task on larger datasets before drawing definitive conclusions would be ideal, especially with my use of the train and test data split, but all findings while doing this assignment corroborates the idea that there is no relationship between horoscopes and descriptive terms.

# Individual Assignment
### By Carl-Emil Schjøtt Kramshøj, Programming for the Humanities, 2022 
### Introduction
