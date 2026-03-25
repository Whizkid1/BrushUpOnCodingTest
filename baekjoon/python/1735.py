# 교훈... 문제를 똑바로 읽자....
# 주어진 분수를 그대로 합하여(기약분수로 바꾸지 X)
# 합한 값을 기약분수로 해라....
from math import lcm
from math import gcd

a, A = map(int, input().split())
b, B = map(int, input().split())

def i_f(s, ss):
    g = gcd(s, ss)
    if g != 1:
        s = s//g
        ss = ss//g
    return s, ss

# a, A = i_f(a, A)
# b, B = i_f(b, B)
nAB = lcm(A, B)
na = a*(nAB//A)
nb = b*(nAB//B)
nab = na + nb
nab, nAB = i_f(nab, nAB)
print(nab, nAB)
