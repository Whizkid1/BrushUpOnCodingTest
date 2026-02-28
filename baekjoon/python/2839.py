n = int(input())
fmc = (n//5)+1
tmc = (n//3)+1
ans = 0
for i in range(tmc):
    temp = n - 3*i
    if (temp%5) == 0: # 무조건 5로만 채운 개수가 제일 작다는 아이디어
       ans += (temp//5)
       ans += i
       break
if ans == 0:
    ans = -1
print(ans)