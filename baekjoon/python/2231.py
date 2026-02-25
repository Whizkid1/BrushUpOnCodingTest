n = int(input())
ans = 0
for i in range(n):
    temp = 0
    temp += i
    for j in range(len(str(i))):
        temp += int(str(i)[j])
    if temp == n:
        ans = i
        break
print(ans)