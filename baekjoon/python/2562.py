l = []
for i in range(9):
    n = int(input())
    l.append(n)
# l = [int(input()) for i in range(9)]

mx = max(l)
print(mx)
print(l.index(mx)+1)

