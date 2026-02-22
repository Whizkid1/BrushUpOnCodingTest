n, m = map(int, input().split())
l = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    rl = l[i-1:j]
    rl = rl[::-1]
    l[i-1:j]=rl
    # l[i-1:j] = l[i-1:j][::-1]
    # l[i-1:j] = l[i-1:j:-1] # 이렇게는 안됨....
print(*l)