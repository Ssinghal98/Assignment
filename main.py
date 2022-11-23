
import random
import loading
import validator
import readwrite


#functions for ANSI colors : 
def red(str1):
    return "\033[31m {}\033[00m".format(str1)

def green(str1):
    return "\033[32m {}\033[00m".format(str1)

def blue(str1):
    return "\033[34m {}\033[00m".format(str1)

#functions to check if the question was already asked ??
    
def checkquestion(str3):
    val = 0
    linearray = readwrite.existingquestion()
    for x in range(len(linearray)):
        if str3 == linearray[x] :
            val = val + 1
            if val >= 2 :
                boolval = True
    # print(boolval)
    return val

#main
def main () :
    print("Welcome to magic 8 ball! \n")
    print("Loading all the magical responses")
    loading.loading()
        # 1st question
    testques = input("Ready? Ask me a question \n")
    readwrite.writequestions(validator.stringval(testques))
    answerlist = readwrite.datareader()
    answerstr = random.choice(answerlist)
    mylist = [red(answerstr), green(answerstr), blue(answerstr)]
    print("Magic 8 Ball says: \t")
    loading.thinking()
    print(random.choice(mylist))
        #repeated questions
    while(True):
            
        teststr = input("Press 1 to ask another question or Press 2 to exit \n")

        if teststr == '1':
            teststr1 = input("Ask another question \n")
            #enter a validator here for question
            readwrite.appendquestions(validator.stringval(teststr1))
            if checkquestion (teststr1) >= 2:
                print ("You've already asked this question, Ask another question  \n")
                while(True):
                    teststr2 = input("Ask me a question \n")
                    readwrite.appendquestions(validator.stringval(teststr2))
                    if checkquestion(teststr2) >= 2:
                        print ("You've already asked this question, Ask another question \n")
                        #add key value 
                        continue
                    else:
                        answerlist = readwrite.datareader()
                        answerstr = random.choice(answerlist)
                        mylist = [red(answerstr), green(answerstr), blue(answerstr)]
                        print("Magic 8 Ball says: \t")
                        loading.thinking()
                        print(random.choice(mylist))
                        break
            else:
                answerlist = readwrite.datareader()
                answerstr = random.choice(answerlist)
                mylist = [red(answerstr), green(answerstr), blue(answerstr)]
                print("Magic 8 Ball says: \t")
                loading.thinking()
                print(random.choice(mylist))
            continue

        elif teststr == '2':
            loading.color()
            break
        else:
            print ("Wrong Input!! The input is not 1 or 2 : ")
            continue

#    print ("You typed", (Testques) )

if __name__ == "__main__":
    main()