n, m = map(int, input().split())
s = set([input() for _ in range(n)])
cnt = 0
for i in range(m):
    t = input()
    if t in s:
        cnt += 1

print(cnt)

# set 사용 이유
# 1. 리스트는 시간초과
# 2. 문제 힌트: 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.
