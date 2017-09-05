def prime_factor(a):
    temp = a
    list = []
    for i in range(2, int(temp / 2)):
        if temp % i == 0:
            list.append(i)
            temp = temp / i

    print(list)


def while_prime_factor(a):
    list = []
    factor = 2
    for i in range(2, factor**2 <= a ):
        factor = i
        print("factor: "+ str(factor))
        while( a % factor == 0):
            list.append(factor)
            a = int(a/factor)
            print("a: " + a + " factor: " + factor)
    print(list)


def main():
    prime_factor(13195)
    print("Inna metoda")
    while_prime_factor(13195)


main()
