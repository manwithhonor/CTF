import telnetlib

HOST = "51.68.126.197"
PORT = 5556

def parse(s):
    num = [0]
    sign = []
    for c in s:
        if ord('0') <= c <= ord('9'):
            num[-1] *= 10
            num[-1] += c - ord('0')
        elif chr(c) != ' ':
            sign.append(chr(c))
            num.append(0)
    a, b = num[0], num[1]
    if sign[0] == '+':
        return str(a + b)
    elif sign[0] == '-':
        return str(a - b)
    elif sign[0] == '*':
        return str(a * b)
    elif sign[0] == '/':
        return str(a // b)


telnet = telnetlib.Telnet()
telnet.open(HOST, PORT)
here = ''
for i in range(100):
    here = telnet.read_until(b"/100\n")
    print(here)
    kek = telnet.read_until(b"=")
    print(kek)
    res = parse(kek)
    telnet.write((res + '\n').encode())
print(here)
here = telnet.read_all()
print(here)