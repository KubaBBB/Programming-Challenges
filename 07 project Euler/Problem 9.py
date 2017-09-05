# a< b <c
# a^2 + b^2 = c^2
# c = 1000 - a - b
#
#   find a*b*c
#


def func():
    global c
    stat = 1000
    for a in range(1,stat +1 ):
        for b in range(1,stat+1):
            c = stat - a - b
            if c**2  == a**2 + b**2:
                print("a: " + str(a) +" b: " +str(b)+" c: "+str(c))
                print(str(a * b * c))


if __name__ == '__main__':
    func()