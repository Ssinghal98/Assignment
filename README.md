#I, Suyash Singhal 000815903, certify that this material is my original work. No other person's work has been used without due acknowledgment and I have not made my work available to anyone else.

Assignment for Python for Networking - COMP-10247

The program is based off the Magic 8 ball

Overview : 
Input is taken from a response file and all the respnses are written into a list with the help of datareader function in readwrite module
The responses file includes a list of 30 responses having a mix of affirmative, non-committal and negative sentences
All the file commands have been coded to handle the filenotfounderror exceptions
The script is interactive and users can ask any form of yes/no questions 
Random module is then used to pick an answer from the 30 possible responses
When a question is asked by the user, a random responses is generated with the help of that random module
Additionally, questions are recorded in a different file called questions.txt to make sure questions are not repeated

Modules used : 
OS : for the file input/output
Time : to generate some cool visual effects on loading/thank you prompt
Validator : To check the input string from the user and re prompt if the input format is incorrect
Loading : visual effects module using ANSI
readwrite : has functions for I/O on responses and questions files

Working : 
Input a yes/no question for the magic 8ball
The string will be validated and the user will be prompted to input again if the format is wrong. Expected format is plain string with no special characters or numbers
if the string is validated, the user enters the GUI
user is asked to input 1 or 2, if the user inputs 1, more questions can be asked and if the user enters 2, the program quits
input validation is also enforced on the numerals 1 and 2, meaning if the user inputs the wrong value, a re-prompt will pop up
if the user inputs 1, the program checks the questions files to see if the question is repeated
On a repeated question, the user is asked to input a new question 
this loop continues until the user presses 2 to quit the program
on quitting user gets a colored goodbye message
