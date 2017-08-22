import math
from random import randint

def CompareHeight(x,y):
    if x==y:
        print("your height is equal as mine")
    elif x>y:
        print ("You are taller than me")
    elif x<y:
        print ("You are smaller than me")

def SuccesHorT(x,y):
    if x is y:
        print("You win!\n")
        if x is 1:
            print("You choose head and result is head")
        if x is 2:
            print("You choose tail and result is tail")
    if x is not y:
        print("You lose...\n")
        if x is 1:
            print("You choose head and result is tail")
        if x is 2:
            print("You choose tail and result is head")

height = input("Enter your height: ")
my_height = 187
CompareHeight(int(height),my_height)
choice = input("Enter your choice: 1 - head, 2 - tail: ")
rand = randint(1,2)
SuccesHorT(int(choice), rand)


