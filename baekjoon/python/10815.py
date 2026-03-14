import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))
ans = [0 for _ in range(m)]
for i in range(m):
    if ml[i] in nl:
        ans[i] = 1
print(*ans)

# 시간 초과....
# 리스트 자체를 사용하면 안될듯 하다