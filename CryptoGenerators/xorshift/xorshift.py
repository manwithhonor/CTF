import os
import struct

from secret import flag, a, b, c
# flag format: flag{...}


def xorshift32(state, a, b, c):
	state &= 0xffffffff
	state ^= (state >> a) & 0xffffffff
	state ^= (state << b) & 0xffffffff
	state ^= (state >> c) & 0xffffffff
	return state

def xor(a, b):
	return bytes([x ^ y for x, y in zip(a,b)])


if len(flag) % 4:
	print("Flag length must be a multiple of 4.")
	exit(0)

state = struct.unpack('<I', os.urandom(4))[0]

gamma = b''
for i in range(0, len(flag), 4):
	state = xorshift32(state, a, b, c)
	gamma += struct.pack('<I', state)

encrypted = xor(gamma, flag)

with open("flag.enc", 'wb') as f:
	f.write(encrypted)