from PIL import Image

txt = open('password.bmp.enc', 'rb').read()
im = Image.new('RGB', (1920, 1080))


data = {i: 0 for i in range(256)}


def g():
    for i in range(160, len(txt), 16):
        data[txt[i]] += 1

    for i in range(160, len(txt), 16):
        col = int(256 * data[txt[i]] / ((len(txt) - 160) // 16))
        a, b = get(i)
        for j in range(8):
            im.putpixel(((a + j), 1080 - b - 1), col)


def get(i):
    ti = (i - 160) // (1920 * 2)
    tj = (i - 160) % (1920 * 2) // 2
    # return ti, tj
    # return 1079 - tj, 1919 - ti
    return tj, ti


def get1(i):
    ti = i // 1080
    tj = i % 1080
    return ti, tj


# for i in range(1920 * 1080):
    # if get1(i)[1] < 1080 // 2:
    #     im.putpixel(get1(i), int(256 * i / (1920 * 1080)))
    # else:
    #     im.putpixel(get1(i), 256 - int(256 * i / (1920 * 1080)))r

g()
# im.rotate(180).show()
im.show()
# l = [(data[i], i) for i in range(256)]
# l.sort(reverse=True)
# print(l)