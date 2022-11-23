import os

def datareader ():
    try:
        with open ('Responses.txt', 'r') as test:
            lines = test.readlines()
    except FileNotFoundError:
        print("File not found")
    return[line.strip() for line in lines]

def writequestions(str2):
    newstr = str2 + "\n"
    try:
        if os.path.exists('Questions.txt') == True:
            with open('Questions.txt', 'w') as test:
                test.write(newstr)
        else:
            with open('Questions.txt', 'w+') as test: #to make the file readable?
                test.write(newstr)
    except FileNotFoundError:
        print("File not found")

def appendquestions(str3):
    newstr = str3 + "\n"
    try:
        with open('Questions.txt', 'a') as test:
            test.write(newstr)
    except FileNotFoundError:
        print("File not found")

def existingquestion():
    val = 0
    try:
        with open('Questions.txt', 'r') as test:
            lines = test.readlines()
    except FileNotFoundError:
        print("File not found")
    return[line.strip() for line in lines]