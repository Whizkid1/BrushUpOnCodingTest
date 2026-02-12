m = int(input())
n = int(input())
a = []
for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            break
    else:
        a.append(i)
a.sort()
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(a[0])