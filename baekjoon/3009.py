xl = []
yl = []
for _ in range(3):
    x, y = map(int, input().split())
    if x not in xl:
        xl.append(x)
    else:
        xl.remove(x)
    if y not in yl:
        yl.append(y)
    else:
        yl.remove(y)
print(*xl)
print(*yl)