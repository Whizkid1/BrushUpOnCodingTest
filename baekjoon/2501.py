n, k = map(int, input().split())
divisorsList = []
for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        divisorsList.append(i)
        if (i ** 2) != n:
            divisorsList.append(n // i)
divisorsList.sort()

if k > len(divisorsList):
    print(0)
else:
    print(divisorsList[k-1])