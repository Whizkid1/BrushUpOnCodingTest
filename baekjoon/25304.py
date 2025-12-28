answer = int(input())
n = int(input())
total = 0

for i in range(n):
    p, a = input().split()
    p, a = int(p), int(a)
    total += p * a

if total == answer :
    print("Yes")
else :
    print("No")