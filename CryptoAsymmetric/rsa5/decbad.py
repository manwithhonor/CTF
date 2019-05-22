import math
from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse
from Crypto.PublicKey import RSA
from numpy import product

def chinese_remainder(n, a):
    sum = 0
    prod = product(n)
    
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * inverse(p, n_i) * p
    return sum % prod

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

flag_cubed = chinese_remainder([key[i].n for i in range(3)], r)
flag = root(flag_cubed)

print(long_to_bytes(flag))
