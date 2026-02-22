arr = [0] * 10000
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        arr[(x+i)*100+y:(x+i)*100+y+10] = [1]*10

print(arr.count(1))