from PIL import Image
import itertools
from pyzbar.pyzbar import decode
# import qrtools

im = [Image.open('qr' + str(i) + '.png') for i in range(1, 10)]

n = 66

res = [-1] * 9
res[0] = 2
res[2] = 8
res[6] = 5
res[8] = 4
res[3] = 7
res[1] = 1

for p in list(itertools.permutations([0, 3, 6])):
    j = 0
    for i in [4, 5, 7]:
        res[i] = p[j]
        j += 1
    hereimg = Image.new(im[0].mode, (n * 3, n * 3))
    for i in range(3):
        for j in range(3):
            for ii in range(n):
                for jj in range(n):
                    hereimg.putpixel((j * n + jj, i * n + ii), im[res[i * 3 + j]].getpixel((jj, ii)))
    # hereimg.save('temp.png', 'png')
    # d = qrtools.QR()
    # d.decode('temp.png')
    # print(d.data)
    # print(decode(hereimg))
    hereimg.show()
    # break