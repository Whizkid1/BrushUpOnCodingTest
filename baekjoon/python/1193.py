n = int(input())
ep=1
ad=1
while n>ep:
    ad+=1
    ep+=ad
if ad%2 == 1:
    print(f'{1+(ep-n)}/{ad-(ep-n)}')
else:
    print(f'{ad-(ep-n)}/{1+(ep-n)}')

# 나의 경우 몇번째 그룹인지 확인 후, 짝수 규칙과 홀수 규칙에 맞춰서 출력되게 했다.
# 나의 풀이를 더 깔끔하게 정리... 다른사람 풀이
# 1/1                           1번째줄 (나: 1번 그룹)
# 1/2, 2/1                      2번째줄 (나: 2번 그룹)
# 3/1, 2/2, 1/3                 3번째줄
# 1/4, 2/3, 3/2, 4/1
# 5/1, 4/2, 3/3, 2/4, 1/5
# ...
# 몇번째 줄에 몇번째 위치의 분수가 무엇인지 알아내기
# num = int(input())
# line = 1
# while num > line:
#     num -= line
#     line += 1
# 출력 규칙
# # 짝수일경우
# if line % 2 == 0:
#     a = num
#     b = line - num + 1
# # 홀수일경우
# elif line % 2 == 1:
#     a = line - num + 1
#     b = num
#
# print(f'{a}/{b}')