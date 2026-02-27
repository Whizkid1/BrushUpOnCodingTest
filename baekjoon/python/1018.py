n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
# ans = 0
# for i in range(n-8):
#     for j in range(m-8):
#         tarr = [row[j:j+8] for row in arr[i:i+8]]
print(arr)

# # 고민시간 1시간 초과
# # 실패 원인 -> 인덱스 별 B & W 의 구분자 카운트 아이디어 고갈
# # --> 특히 B로 시작하는 줄의 다음 줄은 시작이 W로 카운트 하는 방법
# n,m = map(int, input().split())
# original = []
# count = []
#
# for _ in range(n):
#     original.append(input())
#
# for a in range(n-7):
#     for b in range(m-7):
#         white_index = 0 # 흰색으로 시작
#         black_index = 0 # 검정으로 시작
#         for i in range(a,a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         white_index += 1
#                     if original[i][j] != 'B':
#                         black_index += 1
#                 else:
#                     if original[i][j] != 'B':
#                         white_index += 1
#                     if original[i][j] != 'W':
#                         black_index += 1
#         count.append(min(white_index, black_index))
#
# print(min(count))