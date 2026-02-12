# n = int(input())
#
# def find_decimal(n):
#     l = []
#     for i in range(1, n):
#         if i == 1:
#             continue
#         for j in range(2, int(i ** (1 / 2)) + 1):
#             if i % j == 0:
#                 break
#         else:
#             l.append(i)
#     return l

# 다른 문제 풀이
# 1. 주어진 n보다 작은 소수를 모두 찾고
# 2. 반복문으로 제일 작은 소수부터 하나씩 여러번 나누고 출력
# 3. 나머지가 생기면 다음 소수로
# -> 생각해보면 소수로 충분히 여러번 나누면 소수들의 곱만 남는디... 어렵게 생각했다 또
num = int(input())
i = 2
while num > 1:
    if num % i == 0:
        num = num // i
        print(i)
    else:
        i += 1