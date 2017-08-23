def Age2Sec(x):
    sec = 0
    for i in range(0,x):
        sec = sec + 365*24*60*60
        if x%4 is 0:
            sec = sec + 24*60*60
    print("age: "+str(x)+" Seconds: "+str(sec))

age = input("Enter your age")
Age2Sec(int(age))