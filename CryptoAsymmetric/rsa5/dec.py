from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse
from Crypto.PublicKey import RSA
from numpy import product
from binascii import hexlify

def root(n):
    l, r = 1, n
    while l < r - 1:
        m = (l + r) // 2
        if m ** 3 <= n:
            l = m
        else:
            r = m
    return l

key = [RSA.importKey(open('key.pub.' + str(i)).read()) for i in range(1, 4)]
r = [bytes_to_long(open('flag.txt.enc.' + str(i), 'rb').read()) for i in range(1, 4)]
npr = product([key[i].n for i in range(3)])
ns = [npr // key[i].n for i in range(3)]
ms = [inverse(ns[i], key[i].n) for i in range(3)]
flag = sum([r[i] * ms[i] * ns[i] for i in range(3)]) % npr

fr = root(flag)

text = long_to_bytes(fr)
print(text)
