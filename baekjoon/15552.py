import sys

n = sys.stdin.readline()
n = int(n)
for i in range(n):
    a, b = sys.stdin.readline().split()
    a, b = int(a), int(b)
    print(a + b)
