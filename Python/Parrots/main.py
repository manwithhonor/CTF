from bs4 import BeautifulSoup
import requests

base = 'http://51.68.126.197:51337'
parr = '/parrots?level='
topass = '&password='
now = base

i = 1

i = 50
now = 'http://51.68.126.197:51337/parrots?level=50&password=8e8614058f111bbca1c2dc18cd46a58fe3b8fff8e4f157c0e0845b'

i = 91
now = 'http://51.68.126.197:51337/parrots?level=91&password=c65d0872f955f2d237b226e1cf43ac519686b6bf3128bc9580c698'

while True:
    i += 1
    lol = requests.get(now)
    soup = BeautifulSoup(lol.text, 'lxml')
    if i <= 11:
        t = soup.a['href']
        now = base + t
    elif i <= 50:
        password = ''.join(soup.div.h3.text.split()).split(':')[1]
        now = base + parr + str(i) + topass + password
    elif i <= 90:
        for c in soup.div.find_all('h2'):
            password = ''.join(c.text.split())
            now = base + parr + str(i) + topass + password
            kek = requests.get(now)
            keksoup = BeautifulSoup(kek.text, 'lxml')
            if not keksoup.div.find('a'):
                break
    else:
        password = ''
        for c in soup.div.find_all('img'):
            password += c['alt']
        now = base + parr + str(i) + topass + password
    print(i, 'done?')
    print(now)