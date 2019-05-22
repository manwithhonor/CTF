from Crypto.Cipher import DES
import os
import base64
import sys

def pad(s):
	bs = 8
	return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
	return s[:-ord(s[len(s)-1])]

def encrypt(s):
	key = os.urandom(8)
	cipher = DES.new(key, DES.MODE_ECB)
	return (cipher.encrypt(pad(s)), base64.b64encode(key))

def decrypt(s, key):
	key = base64.b64decode(key)
	cipher = DES.new(key, DES.MODE_ECB)
	return unpad(cipher.decrypt(s))

if len(sys.argv) != 2:
	print "Usage: %s <filename>"%(sys.argv[0])
	exit(1)

buf = open(sys.argv[1], 'rb').read()
enc,key = encrypt(buf)
print 'Your key is %s'%(key)
open(sys.argv[1] + '.enc', 'wb').write(enc)
print 'File %s was encrypted'%(sys.argv[1])
