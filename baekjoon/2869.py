# 100 99 1000000000 -> 엄청 오래 걸림.... timeout 예상....
# 다른 풀이 생각해야함
# a, b, v = map(int, input().split())
# n = 0
# d = 0
# while 1:
#     d += 1
#     n += a
#     if n >= v:
#         break
#     n -= b
# print(d)
a, b, v = map(int, input().split())
print(v-a+(a-b))