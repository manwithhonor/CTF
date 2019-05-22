from hashlib import md5
import base64
import string
import random
import sys
import os

f = open('text.txt.enc', 'rb')

lines = []

maxi = 0

for line in f:
    lines.append(base64.b64decode(line))
    maxi = max(maxi, len(lines[-1]))

rows = []
hx = []
skip = [1] * maxi

# skip[0] = 25
# skip[0] = 28
# skip[1] = 14

for i in range(maxi):
    rows.append([])
    for l in lines:
        if len(l) > i:
            rows[i].append(l[i])
        else:
            rows[i].append(-1)
    here = {i: 0 for i in range(256)}
    for c in rows[i]:
        if c == -1:
            continue
        here[c] += 1
    lst = []
    for c in here:
        lst.append([here[c], c])
    lst.sort(reverse=True)
    ch = 'e'
    hx.append(lst[0][1] ^ ord(ch))
    # was = False
    # for xor in range(256):
    #     ok = 1
    #     for cc in rows[i]:
    #         if cc == -1:
    #             continue
    #         c = cc ^ xor
    #         if not 32 <= c <= 127:
    #             ok = 0
    #             break
    #         # if i == 0 and chr(c) not in string.ascii_uppercase and chr(c) not in ['\'', '"', '-']:
    #         #     ok = 0
    #         #     break
    #         # if not (chr(c) in string.ascii_letters or chr(c) in string.digits or chr(c) == ' '):
    #         # if char(c)
    #
    #             # ok = False
    #             # break
    #     skip[i] -= ok
    #     if not skip[i]:
    #         hx.append(xor)
    #         was = True
    #         break
    # if not was:
    #     hx.append(0)


# for line in lines:
    # lasts[len(line) - 1].append(line[-1])
    # if 4 * len(line) < 3 * maxi:
    #     continue
    # hx[len(line) - 1] = line[-1] ^ ord('.')

for line in lines:
    nline = b''
    for i in range(len(line)):
        nline += chr(line[i] ^ hx[i]).encode()
    # for c in nline:
    #     if 33 <= ord(c) <= 128:
    #         print(c, end='')
    #     else:
    #         print('_')
    # print()
    for c in nline:
        if 32 <= c <= 127:
            print(chr(c), end='')
        else:
            print('.', end='')
    print()
    # print(nline)
