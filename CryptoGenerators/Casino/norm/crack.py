import telnetlib
import time
import mt

ip = '51.68.126.197'
port = 45033


def readNumber():
    tn = telnetlib.Telnet(ip, port)
    tn.read_until(b': ')
    tn.write(b'0\n')
    tn.read_until(b': ')
    tn.write(b'1000000000\n')
    tn.read_until(b': ')
    tn.write(b'0\n')
    tn.read_until(b': ')
    tn.write(b'0\n')
#    tn.read_until(b'was ')
#    s = tn.read_until(b'\n')
    print(s)


