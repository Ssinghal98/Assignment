import time
import sys


def red(str1):
    return "\033[31m {}\033[00m".format(str1)

def green(str1):
    return "\033[32m {}\033[00m".format(str1)

def blue(str1):
    return "\033[34m {}\033[00m".format(str1)

st = time.time()

seconds = 10

def loading():
    while True:
        ct = time.time()
        loopduration = ct - st

        sys.stdout.write('\rloading.')
        time.sleep(0.1)
        sys.stdout.write('\rloading..')
        time.sleep(0.1)
        sys.stdout.write('\rloading...')

        if loopduration > seconds:
            break


tt = time.time()

def thinking():
    while True:
        ct = time.time()
        loopduration = ct - tt

        sys.stdout.write('\rThinking /')
        time.sleep(0.2)
        sys.stdout.write('\rThinking -')
        time.sleep(0.2)
        sys.stdout.write('\rThinking \\')
        time.sleep(0.2)
        sys.stdout.write('\rThinking |')
        time.sleep(0.05)
        sys.stdout.write('\rThinking :')
        time.sleep(0.05)
        sys.stdout.write('\r')
        if loopduration > 20:
            break

cot = time.time()
seconds = 10

def color():
    while True:
        ct = time.time()
        loopduration = ct - cot

        sys.stdout.write('\r\033[31mThank You for Playing! Goodbye\033[00m')
        time.sleep(0.1)
        sys.stdout.write('\r\033[32mThank You for Playing! Goodbye\033[00m')
        time.sleep(0.1)
        sys.stdout.write('\r\033[33mThank You for Playing! Goodbye\033[00m')
        time.sleep(0.1)
        sys.stdout.write('\r\033[34mThank You for Playing! Goodbye\033[00m')
        
        if loopduration > 60:
            break

    