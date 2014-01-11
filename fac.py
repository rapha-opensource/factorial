#!/usr/bin/env python3.3

import random
import math
import zlib
import pickle

def fact2(n):
    result = 1
    for i in range(n):
        result *=(i+1)
    return result


def it(n):
    c=0
    while c<n:
        yield random.randint(0,255)
        c+=1

n = int.from_bytes(bytearray(it(200)), 'big')

def ff(n, size, compression):
    """ returns the decomposition of n in a factorials base """
    factors = []
    remainder = n
    while remainder > 0:
        k = 1
        last_factorial = 1
        new_factorial = 1
        while new_factorial <= remainder:
            k += 1
            last_factorial = new_factorial
            new_factorial = math.factorial(k)
        k -= 1
        a = int( remainder / last_factorial )
        factors += [(k, a)]
        remainder = remainder % last_factorial
        # estimate the compression factor 
        factors += [(0, remainder)]
        compression += [int(100*len(zlib.compress(pickle.dumps(factors)))/size)]
        factors.pop()
        if remainder == 1:
            factors += [(0, 1)]
            break
    return factors


def expand_factors(factors):
    res = 0
    for f in factors:
        res += f[1]*math.factorial(f[0])
    return res

c = []
f = ff(n, 200, c)
print( f )
print( len(f) )
print( expand_factors(f) == n )
print(c)

# expecting [(4,2), (2, 1)]

