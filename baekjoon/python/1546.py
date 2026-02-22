# print(((40/80*100)+(80/80*100)+(60/80*100))/3)
n = int(input())
ts = list(map(int, input().split()))
ms = max(ts)
result = 0
for i in ts:
    result += i/ms*100
print(result/n)

# 미친 풀이....
# n = int(input())
# l=[int(i) for i in input().split()]
# print(sum(l)/max(l)*100/n)