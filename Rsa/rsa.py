from esponenziazioneVeloce import expVeloce
from euclide import euclideEsteso
import random


def encrypt(m, keys):
    return expVeloce(m, keys[0], keys[1])


def decrypt(c, keys):
    return expVeloce(c, keys[0], keys[1])


def coPrime(n):
    c = random.randint(2, n)
    while euclideEsteso(c, n)[0] != 1:
        c = random.randint(2, n)
    return c


def generateKey(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = coPrime(phi)
    e = euclideEsteso(d, phi)[1]
    kp = (e, n)
    km = (d, n)
    return kp, km


def generateKeyCrt(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = coPrime(phi)
    e = euclideEsteso(d, phi)
    dp = d % (p - 1)
    if dp < 0:
        dp = dp + p - 1
    dq = d % (q - 1)
    if dq < 0:
        dq = dq + q - 1
    qInv = euclideEsteso(q, p)[1]
    kp = (e[1], n)
    km = (p, q, dp, dq, qInv)
    return kp, km


def decryptCrt(c, km):
    m1 = expVeloce(c, km[2], km[0])
    m2 = expVeloce(c, km[3], km[1])
    h = km[4] * (m1 - m2) % km[0]
    return m2 + h * km[1]

public_key, private_key = generateKey(3, 11)
print(encrypt(8, public_key))
print(decrypt(encrypt(8, public_key), private_key))
public_key, private_key = generateKeyCrt(3, 11)
encr = encrypt(8, public_key)
print(encr)
print(decryptCrt(encr, private_key))
# print coPrime(20)