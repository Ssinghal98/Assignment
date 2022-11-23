import os
import random
import string

def stringval ( str1 ):
    str2 = str1.lower()
    str3 = str2.strip()
    str4 = str3.replace(" ","")
    while str4.isalpha () == False:
        print ("Input is not a valid string, please remove special characters and/or numbers and ask the question again")
        str4 = input().strip().lower().replace(" ","")

    if str2.find('?') == -1:
        str2 = str2 + '?'

    return str2
