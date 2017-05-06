import random
from rabin import rabinTest


def isPrime(r):
    baton = random.randint(1, r)
    return not rabinTest(baton, r)


def generate(bottom, top):
    r = random.randint(bottom, top)
    while r % 2 == 0 or not isPrime(r):
        r = random.randint(bottom, top)
    return r

print generate(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
