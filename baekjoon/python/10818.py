n = int(input())
l = list(map(int, input().split()))
mmax = max(l)
mmin = min(l)
print(mmin, mmax)

## 다른 풀이 222
n = int(input())
l = list(map(int, input().split()))
max = l[0]
min = l[0]
for i in l:
    if i > max:
        max = i
    if min > i:
        min = i
print(min, max)

## 다른 풀이 333
import sys
n, *m = map(int, sys.stdin.read().split())
print(min(m), max(m))
