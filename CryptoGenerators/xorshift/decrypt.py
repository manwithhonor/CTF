from Crypto.Util.number import bytes_to_long, long_to_bytes
import struct

def xorshift32(state, a, b, c):
    state &= 0xffffffff
    state ^= (state >> a) & 0xffffffff
    state ^= (state << b) & 0xffffffff
    state ^= (state >> c) & 0xffffffff
    return state

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a,b)])

enc = open('flag.enc', 'rb').read()
begin = b'flag'

base = bytes_to_long(xor(begin, enc[:4])[-1::-1])
#print(xor(begin, enc[:4]))
#print(bytes_to_long(xor(begin, enc[:4])))
#print(struct.pack('<I', bytes_to_long(xor(begin, enc[:4]))))
print(xor(struct.pack('<I', base), enc[:4]))

for a in range(33):
    for b in range(33):
        for c in range(33):
            gamma = b''
            state = base
            for i in range(0, len(enc), 4):
                gamma += struct.pack('<I', state)
                state = xorshift32(state, a, b, c)
            flag = xor(gamma, enc)
            if flag[4] == ord('{') and flag[-1] == ord('}'):
                print(flag)
#            print(flag)

