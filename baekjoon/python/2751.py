## 두 방법 모두 정답이지만 input을 다른 툴로 받아야 함
## import sys
## input=sys.stdin.readline

# # 시간초과
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# l.sort()
# for _ in l:
#     print(_)

## 시간 초과
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for _ in range(n):
    m = min(l)
    l.remove(m)
    print(m)