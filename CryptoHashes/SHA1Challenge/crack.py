def pad(data):
    bytes = ""

    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    pBits = bits
    #pad until length equals 448 mod 512
    while len(pBits)%512 != 448:
        pBits+="0"
    #append the original length
    pBits+='{0:064b}'.format(len(bits)-1)
    return pBits

from binascii import unhexlify
from base64 import b64encode

message = 'a' * 13 + 'guest'
print(hex(int(pad(message), 2))[2:])
message = unhexlify(hex(int(pad(message), 2))[2:]) + b'admin'
# ans = sha1('admin', 0xbc5dcb07, 0x90b4d8f1, 0x949c5dc5, 0x7b1e1b93, 0xb5cf02d5)
print(message[13:])
print(b64encode(message[13:]))
# print(ans)
