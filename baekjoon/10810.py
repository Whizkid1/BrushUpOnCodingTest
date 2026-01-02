n, m = map(int, input().split())
l = [0 for i in range(n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    l[i:j+1] = [k] * (j-i+1)
print(*l[1:])
