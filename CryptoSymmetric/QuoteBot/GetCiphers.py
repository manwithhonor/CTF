import requests
from base64 import b64encode as enc
from base64 import b64decode as dec

url = 'http://vps595401.ovh.net:47026/change-name'

s = b'AAAA\x04\x00\x00\x00type\x05\x00\x00\x00admin\x04\x00\x00\x00name\x0c\x00\x00\x00aaaaaaaaaaaa'

r = requests.post(url, data={'name': enc(s)})
here = r.cookies.get('session')
print(r.text)
here = dec(here)
here = here[16 * 2:]
here = enc(here)
print(here)
