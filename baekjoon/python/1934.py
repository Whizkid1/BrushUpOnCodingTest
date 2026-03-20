def prime_factors(n):
    factors = []
    d = 2
    # n의 제곱근까지 반복 (효율성)
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    # 남은 n이 1보다 크면 그 자체도 소인수
    if n > 1:
        factors.append(n)
    return factors
from math import prod
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(a*b)
        continue
    pa = prime_factors(a)
    pb = prime_factors(b)
    plcm = []
    for i in pa:
        if i in pb:
            plcm.append(i)
            pb.remove(i)
    lcm = prod(plcm)
    print(int(a*b/lcm))

# 최소공배수, 최대공약수, 소인수분해는 사람마다 풀이 방법이 다양하다...
# 백준의 정답 혹은 구글에서 다양한 방식을 찾아보도록!!(나에게 하는말)
# https://lazy-man.tistory.com/59
# https://llo12346.tistory.com/46