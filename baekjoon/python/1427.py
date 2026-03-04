import sys
input = sys.stdin.readline
c = [0 for _ in range(10)]
n = input().strip()
for i in n:
    idx = int(i)
    c[idx] += 1
ans = ""
for j in range(10):
    if c[j] != 0:
       ans = str(j) * c[j] + ans
print(int(ans))