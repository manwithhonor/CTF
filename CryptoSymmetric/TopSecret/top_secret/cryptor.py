from Crypto.Cipher import DES
import os
import base64
import sys
import string
import random

def pad(s):
	bs = 8
	return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
	return s[:-s[len(s)-1]]

def encrypt(s):
	key = ''.join([random.choice(string.ascii_lowercase) for _ in xrange(8)])
	cipher = DES.new(key, DES.MODE_ECB)
	return (cipher.encrypt(pad(s)), key)

def decrypt(s, key):
	key = key
	cipher = DES.new(key, DES.MODE_ECB)
	return unpad(cipher.decrypt(s))

#if len(sys.argv) != 2:
#    print "Usage: %s <filename>"%(sys.argv[0])
#    exit(1)

	
#buf = open(sys.argv[1], 'rb').read()
#enc,key = encrypt(buf)
#print 'Your key is %s'%(key)
#open(sys.argv[1] + '.enc', 'wb').write(enc)
#print 'File %s was encrypted'%(sys.argv[1])

key = 'cjzyjmnc'
s = open('top_secret.txt.enc', 'rb').read()
print(decrypt(s, key))
