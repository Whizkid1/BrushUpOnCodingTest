n = int(input())
c = 0
s = 1
e = 1
while 1:
    if s <= n <= e:
        break
    c += 1
    s = e + 1
    e = e + (6 * c)
print(c+1)

# 내가 푼 코드는 아래로 간출일 수 있다....
# n = int(input())
#
# nums_pileup = 1  # 벌집의 개수, 1개부터 시작
# cnt = 1
# while n > nums_pileup :
#     nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
#     cnt += 1  # 반복문을 반복하는 횟수
# print(cnt)