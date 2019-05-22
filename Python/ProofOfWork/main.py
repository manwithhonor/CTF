import telnetlib
from hashlib import sha256

telnet = telnetlib.Telnet()

HOST = '51.68.126.197'
PORT = 5555

telnet.open(HOST, PORT)

s = telnet.read_until(b'X = ')
s = s.decode().split('\'')[1]
num = int(s, 16) << 32
print(s)
now = 0
iter = 2**32
for i in range(iter):
    kek = hex(num + i)[2:]
    here = int(sha256(kek.encode()).hexdigest(), 16)
    if here & (2 ** 20 - 1) == 0:
        print(kek, here)
        print(kek[8:])
        telnet.write((kek[8:] + '\n').encode())
        ans = telnet.read_all()
        print(ans)
        break
    if int(i / iter * 100) > now:
        now = int(i / iter * 100)
        print(str(now) + '%')

