a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
while ((a1*n0+a0) <= (c*n0)) :
    n0 += 1
    if n0 == 101:
        break
if n0 == 101:
    print(1)
else:
    print(0)

# # 기울기를 활용한 풀이
# a1,a0=map(int,input().split())
# c=int(input())
# n=int(input())
# if c>=a1 and c*n>=a1*n+a0: # 기울기를 활용하면 반복문을 사용할 필요가 없음
#     print("1")
# else:
#     print("0")

# # 위의 코드 숏코딩 버전
# a,b,c,n=map(int,open(0).read().split())
# print(+(a*n+b<=c*n>=a*n))