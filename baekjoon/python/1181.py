import sys
input = sys.stdin.readline
s = set()
n = int(input())
for _ in range(n):
    s.add(input().strip())
s = sorted(s, key=lambda x : (len(x), x))
for i in s:
    print(i)