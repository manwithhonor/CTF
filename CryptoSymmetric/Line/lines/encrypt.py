#!/usr/bin/env python3
from hashlib import md5
import base64
import random
import sys
import os

# from key import SECRET_KEY
SECRET_KEY = b'lol'

key = int(md5(SECRET_KEY).hexdigest(), 16)


def encrypt(text):
    random.seed(key)
    return base64.b64encode(bytes([a ^ random.randint(0, 255) for a in text]))


# if len(sys.argv) < 2:
#     print("Usage: {} <filename to encrypt>".format(sys.argv[0]))

# filename = sys.argv[1]

filename = 'textmy.txt'

with open(filename, 'r') as file_in:
    with open(filename + '.enc', 'wb') as file_out:
        for line in file_in.readlines():
            file_out.write(encrypt(line.encode()) + b'\n')
