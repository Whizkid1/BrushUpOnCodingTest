n = int(input())
if n == 1:
    print(0)
else:
    xl = []
    yl = []
    for i in range(n):
        x, y = map(int, input().split())
        xl.append(x)
        yl.append(y)
    w = max(xl)-min(xl)
    l = max(yl)-min(yl)
    print(w*l)