import json
import base64
import binascii

i = 2
while True:
    f = open('t' + str(i), 'r')
    kok = json.loads(f.read())
    type = kok['type']
    print(type)
    data = kok['data']
    if type == 'base64':
        res = base64.b64decode(data)
    elif type == 'base85':
        res = base64.b85decode(data)
    elif type == 'hex':
        res = bytearray.fromhex(data)
    else:
        print(kok['type'], i)
        break
    i += 1
    f = open('t' + str(i), 'wb')
    f.write(res)
    f.close()
