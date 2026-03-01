l = []
for _ in range(5):
    l.append(int(input()))
l.sort()
s = sum(l)
print(int(s/5))
print(l[2])