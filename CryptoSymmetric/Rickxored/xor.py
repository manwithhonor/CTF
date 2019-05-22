f = open('enc.bin', 'rb')
sf = open('lol.txt', 'rb')
text = f.read()
rest = sf.read()

flags = 'flag{'
flagm = ''
flage = '}'

order = 'ETAOINSHRDLCUMWFGYPBVKXJQZ'

def getflag():
    return flags + flagm + 'a' * (32 - len(flagm)) + flage

# flag = flags + flagm + flage

def decrypt():
    flag = getflag()
    ntext = b''
    for i in range(len(text)):
        # if i % len(flag) < len(flags) or i % len(flag) == len(flag) - 1:
        ntext += chr(text[i] ^ ord(flag[i % len(flag)])).encode()
        # else:
        #     ntext += text[i]
    return ntext


def xor():
    for i in range(min(len(text), len(rest))):
        # print(chr(text[i] ^ rest[i]), end='')
        here = text[i] ^ rest[i]
        if 32 <= here < 128:
            print(chr(here), end='')


def getstat():
    global flagm, flags
    ind = len(flags) + len(flagm)
    flag = getflag()
    dct = {i: 0 for i in range(256)}
    for i in range(ind, len(text), len(flag)):
        dct[text[i]] += 1
    arr = []
    for c in dct:
        arr.append((dct[c], c))
    arr.sort(reverse=True)
    c = ' '
    if ind - len(flags) in {2, 8, 10}:
        c = 'e'
    elif ind - len(flags) in {5}:
        c = ' '

    flagm += chr(arr[0][1] ^ ord(c))
    # print(arr)


for i in range(32):
    getstat()

flag = getflag()
print(flag)
res = decrypt()
for i in range(0, len(res), len(flag)):
    print(res[i:i+len(flag)])
# print(rest.encode())
# print(res.)
xor()
# print(rest)
# print(res)
# print(decrypt())
# for c in range(ord('0'), ord('9')):
#     flagm = chr(c) * 32
#     here = decrypt()
#     if here[len(flags)] == ' ':
#         print(here)
