def isPrime(a):
    count = 0
    for i in range(2,int(a/2)+1):
        if a%i == 0:
            count+=1
    return 0 if count is 0 else 1

def func(a):
    prime_sum = []
    for k in range(2,a):
        if isPrime(k) == 0:
            prime_sum.append(k)
    print(prime_sum)
    print(sum(prime_sum))

if __name__ == '__main__':
    func(100000)