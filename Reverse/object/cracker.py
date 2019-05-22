with open('source', 'rb') as f1:
	with open('cracked', 'wb') as f2:
		f2.write(f1.read().replace(b'\xd9\x45\x08\xd8\xc1', b'\xd9\xeb\xde\xc9\x90'))
