import sys
input = sys.stdin.readline
n = int(input())
p = [() for _ in range(n)]

for i in range(n):
    a, b = input().split()
    p[i] = (int(a), b, i)

p.sort(key=lambda x: (x[0], x[2]))
for pp in p:
    print(pp[0], pp[1])
## 파이썬의 sort() 함수가 가진 'Stable Sort(안정 정렬)' 성질
## 로 인해서 사실 입력 순서를 해줄 필요가 없었다...