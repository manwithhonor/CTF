with open('source', 'rb') as f1:
	with open('cracked', 'wb') as f2:
		f2.write(f1.read().replace(b'\x75\x11', b'\x90\x90'))
