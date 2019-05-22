from Crypto.Util.number import bytes_to_long, GCD, inverse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

def import_key(p_path, q_path, e = 65537):
	p = int(open(p_path).read())
	q = int(open(q_path).read())
	n = p*q
	phin = (p-1)*(q-1)
	d = inverse(e, phin)
	key = RSA.construct((n, e, d, p, q))
	return key

flag = open('flag.txt').read()


key = import_key('p', 'q')

enckey = PKCS1_v1_5.new(key)
enc_flag = enckey.encrypt(flag)

open("key.pub", "w").write(key.publickey().exportKey(format="PEM"))
open("flag.txt.enc", "w").write(enc_flag)

//10960923066637609324777600779779684663633051932144205197151459865286762208432821864078585846891867169213979214357143454515799450717247919435161475303990443
// 11390241758753765516720619890502283590695482637665146138950902221066361207174240855604983750508950133650776621988896396912586632133672919840253678864112897
