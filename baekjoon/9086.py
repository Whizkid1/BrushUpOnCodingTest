n=int(input())
for _ in range(n):
    s=str(input())
    a=s[0]
    a+=s[-1]
    print(a)

# 이렇게 단순히...
# for _ in range(int(input())):
#     a=input();print(a[0]+a[-1])