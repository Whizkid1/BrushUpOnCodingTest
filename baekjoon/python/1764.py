n, m = map(int, input().split())

l = set()
for _ in range(n):
    l.add(input())
d = set()
for __ in range(m):
    s = input()
    if s in l:
        d.add(s)
print(len(d))
print(*sorted(d), sep='\n')