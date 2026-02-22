n = int(input())
q = list(map(int, input().split()))
cnt = 0
for i in q:
    if i == 1:
        continue
    elif i == 2:
        cnt += 1
        continue
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            break
    else:
        cnt+=1
print(cnt)

# # 다른 사람 코드 1....내 코드에서 불필요한 부분 제거 코드....
# n = int(input())
# arr = list(map(int, input().split()))
# count = 0
# for i in arr:
#     if i == 1:
#         continue
#     for v in range(2, i):
#         if i % v == 0:
#             break
#     else:
#         count += 1
# print(count)

# # 다른 사람 코드 2.... 좀 더 그럴싸한 코드
# input()
# l=list(map(int,input().split()))
# if 1 in l: l.remove(1)
# for i in l[::]:
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0: l.remove(i);break
# print(len(l))

