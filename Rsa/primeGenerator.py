import random
from rabin import rabinTest
import timeit


def isPrime(r, k):
    for _ in range(k):
        baton = random.randint(1, r)
        if rabinTest(baton, r) is True:
            return False
    return True


def generate(bottom, top, k):
    r = random.randint(bottom, top)
    n = 0
    while r % 2 == 0 or not isPrime(r, k):
        r = random.randint(bottom, top)
    return r


def wrapper():
    generate(pow(10, 99), pow(10, 100), 16)

# prime = generate(pow(10, 99), pow(10, 100), 32)
# print prime
# print 'cifre', len(str(prime))
print (timeit.timeit(wrapper, number=1))