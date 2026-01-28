n = int(input())
p = 2
for i in range(n):
    p = p + (p-1)
print(p**2)