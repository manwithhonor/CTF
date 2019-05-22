import threading
from threading import Thread

import telnetlib
import time

ip = '51.68.126.197'
port = 45033

# f = time.time()
# s = time.time()
#
# print(f)
# print(s)


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
    tn.read_until(b'was ')
    s = tn.read_until(b'\n')
    print(s)


def getFlag():
    tn2 = telnetlib.Telnet(ip, port)
    tn2.read_until(b': ')
    tn2.write(b'0\n')
    tn2.read_until(b': ')
    tn2.write(b'1000000000\n')
    tn2.read_until(b': ')
    s = input()
    tn2.write((s + '\n').encode())
    tn2.read_until(b': ')
    tn2.write(b'100\n')
    res = tn2.read_until(b'}')
    # res = tn2.read_all()
    print(res)


Thread(target=readNumber()).start()
Thread(target=getFlag()).start()
