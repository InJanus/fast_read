import time
import os


def get_text(fileName):
    # files will go here
    f = open(fileName, "r")
    contents = f.read().split()
    # get the location of spaces

    for i in contents:
        print(i)
        time.sleep(0.1)
        os.system('cls')


get_text('C:/Users/Brian Culberson/Documents/Code/fast_read/logic/test.txt')