with open('antideb', 'rb') as f1:
	with open('antideb_patched', 'wb') as f2:
		f2.write(f1.read().replace(b'\x75\x14\xbf\x20', b'\x74\x14\xbf\x20'))
