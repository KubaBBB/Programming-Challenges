from random import randint

print("Hello in random name generator!")
count = 0
with open('names.txt' , 'r') as f:
    contents = f.readlines()
    count = len(contents)

print("\nRandom name generated is:\n")
print(contents[randint(0, 4945)])


