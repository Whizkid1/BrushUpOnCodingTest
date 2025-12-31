n, a = map(int, input().split())
l = list(map(int, input().split()))
result = ""
for i in l:
    if i < a:
        result += (str(i) + " ")
print(result)

# 나의 이전 풀이
# N, X = map(int, input().split(" "))
# A = list(map(int, input().split(" ")))
#
# ans = [i for i in A if i < X]
# print(*ans)