from random import randint
class Options:
    Paper, Rock, Scissors = range(3)

def Random(a):
    rand = randint(0,3)
    if a is rand:
        return -1
    elif a is 0:
        return 1 if rand is 1 else 0
    elif a is 1:
        return 1 if rand is 2 else 0
    elif a is 2:
        return 1 if rand is 0 else 0

def StrToInt(b):
    if b ==  "Paper":
        return Options.Paper
    elif b == "Rock":
        return Options.Rock
    elif b == "Scissors":
        return Options.Scissors

def res_func(res, val):
    if res is -1:
        print("Draw, Try again\n" + "You choosed: " + val + " ,computer choosed: " + val + ",")
    elif res is 0:
        print("You lose\n")
        if val == "Paper":
            print("You choosed: " + val + ", computer choosed: Scissors,\n")
        elif val == "Rock":
            print("You choosed: " + val + ", computer choosed: Paper,\n")
        elif val == "Scissors":
            print("You choosed: " + val + ", computer choosed: Rock,\n")
    elif res is 1:
        print("You win\n")
        if val == "Paper":
            print("You choosed: " + val + ", computer choosed: Rock,\n")
        elif val == "Rock":
            print("You choosed: " + val + ", computer choosed: Scissors,\n")
        elif val == "Scissors":
            print("You choosed: " + val + ", computer choosed: Paper,\n")


def main():
    in_val = input("Choose your value - Paper,Rock,Scissors\n")
    result = Random(StrToInt(in_val))
    res_func(result , in_val)
    while result is -1:
        in_val = input("Choose other value - Paper,Rock,Scissors\n")
        result = Random(StrToInt(in_val))
        res_func(result , StrToInt(in_val))

main()