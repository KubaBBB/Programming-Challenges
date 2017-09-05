
from math import sqrt,ceil
import numpy as np
def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    #""" Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

if __name__=='__main__':
    import itertools
    import sys

    def test(f1,f2,num):
        print('Testing {f1} and {f2} return same results'.format(
            f1=f1.func_name,
            f2=f2.func_name))
        if not all([a==b for a,b in itertools.izip_longest(f1(num),f2(num))]):
            sys.exit("Error: %s(%s) != %s(%s)"%(f1.func_name,num,f2.func_name,num))

    n = 1000
    test(sieveOfAtkin, primesfrom2to, n)