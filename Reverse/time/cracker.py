with open('source', 'rb') as f1:
	with open('cracked', 'wb') as f2:
		f2.write(f1.read().replace(b'\x00\xca\x9a\x3b', b'\x00\xca\x9a\x77'))
