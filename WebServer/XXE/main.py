import requests

f = open('text.txt', 'r')
text = f.read()

url='http://vps595401.ovh.net:47025'
endu = '/process.php'

# r = requests.get(url)
r = requests.post(url + endu, text)

print(r.text)