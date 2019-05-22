import re

f = open('text.txt', 'r')
text = f.read()
f.close()

s = ['0'] * 37

for p in re.findall("The character number [1-9]*[0-9] in flag is '+[0-9, a-z]'", text):
    p = p[len('The character number '):]
    num = int(p[:2])
    c = p[-2]
    s[num] = c
print(''.join(s))
