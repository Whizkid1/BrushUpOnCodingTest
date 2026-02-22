c = [1,1,2,2,2,8]
r = list(map(int, input().split()))
a = []
for i in range(6):
    a.append(c[i]-r[i])
print(*a)