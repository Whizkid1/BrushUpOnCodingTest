n, b = input().split()
a = 0
for i in range(len(n)):
    ri = -1 * i -1
    if n[ri] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a += (ord(n[ri])-55) * (int(b)**i)
    else:
        a += int(n[ri]) * (int(b)**i)
print(a)