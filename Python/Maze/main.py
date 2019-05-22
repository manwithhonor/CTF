import telnetlib

HOST = '51.68.126.197'
PORT = 5557

telnet = telnetlib.Telnet()

telnet.open(HOST, PORT)

BLOCK, EMPTY, START, FINISH = 0, 1, 2, 3


def buildMaze(s):
    n, m = 0, -1
    for i in range(len(s)):
        if s[i] == '\n':
            n += 1
            if m == -1:
                m = i
    d = [[]] * n
    for i in range(n):
        d[i] = [0] * m
    i, j = 0, 0
    for c in s:
        if c == '\n':
            j = 0
            i = i + 1
            continue
        if c == '@':
            d[i][j] = START
        elif c == '*':
            d[i][j] = FINISH
        elif c == ' ':
            d[i][j] = EMPTY
        else:
            d[i][j] = BLOCK
        j += 1
    return d, n, m


D = 4
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
let = ['d', 's', 'a', 'w']


NOT_USED = '-'


def isCorrect(t, n, m):
    return 0 <= t[0] < n and 0 <= t[1] < m


def findPath(d, n, m):
    s, t = -1, -1
    for i in range(n):
        for j in range(m):
            if d[i][j] == START:
                s = (i, j)
            if d[i][j] == FINISH:
                t = (i, j)
    path = [[]] * n
    for i in range(n):
        path[i] = [NOT_USED] * m
    path[s[0]][s[1]] = ''
    q = [(0, 0)] * (n * m + 10)
    head, tail = 0, 0
    q[head] = s
    head += 1
    while head != tail:
        v = q[tail]
        tail += 1
        if v == t:
            break
        for dt in range(D):
            to = (v[0] + dx[dt], v[1] + dy[dt])
            tor = (to[0] + dx[dt], to[1] + dy[dt])
            if isCorrect(tor, n, m) and d[to[0]][to[1]] != BLOCK and path[tor[0]][tor[1]] == NOT_USED:
                path[tor[0]][tor[1]] = path[v[0]][v[1]] + let[dt]
                q[head] = tor
                head += 1
    return path[t[0]][t[1]]


while True:
    print(telnet.read_until(b'100\n').decode())
    smaze = telnet.read_until(b'>')
    smaze = smaze[:-1].decode()
    # print(smaze)
    d, n, m = buildMaze(smaze)
    res = findPath(d, n, m)
    # print(res)
    telnet.write((res + '\n').encode())
