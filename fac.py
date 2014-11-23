import random
import math
import zlib
import pickle

def it(n):
    c=0
    while c<n:
        yield random.randint(0,255)
        c+=1

n = int.from_bytes(bytearray(it(200)), 'big')

def ff(n):
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
        if remainder == 1:
            factors += [(0, 1)]
            break
    return factors


def expand_factors(factors):
    res = 0
    for f in factors:
        res += f[1]*math.factorial(f[0])
    return res

f = ff(n)
print(n)
print( f )
print( len(f) )
print( expand_factors(f) == n )

