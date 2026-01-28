n = int(input())
for _ in range(n):
    r = int(input())
    q = r//25
    r = r-q*25
    d = r//10
    r = r-d*10
    ni = r//5
    r = r-ni*5
    p = r
    print(q, d, ni, p)
