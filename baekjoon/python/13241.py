# 1. 초 간단 버전 - 라이브러리 사용
from math import lcm
a, b = map(int, input().split())
if a == 1 or b == 1:
    print(a*b)
else:
    print(lcm(a, b))

# 2. 이전 문제 1934 그래로 사용

# 3. 대부분의 풀이 -> 유클리드 호제법 알고리즘 사용
# 유클리드 호제법 풀이 i)귀납법 ii)반복문(나누셈 몫 0 까지)