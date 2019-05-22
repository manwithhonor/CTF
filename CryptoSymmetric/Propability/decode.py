order = 'irbhcxsvRngwutleadypjkfqom'


f = open('smpl.txt.enc', 'r')
text = f.read()
f.close()
text = text.upper()
ntext = ''

count = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
for c in text:
    if 'A' <= c <= 'Z':
        count[c] += 1

lst = []
for key in count:
    lst.append([count[key], key])

dct = {lst[i][1]: order[i] for i in range(len(order))}

lst.sort(reverse=True)

for c in text:
    if 'A' <= c <= 'Z':
        ntext += dct[c]
    else:
        ntext += c
print(ntext)