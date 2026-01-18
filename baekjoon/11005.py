n, b = map(int, input().split())
a=""
while n:
    r = n%b # r, n 서순 때문에 틀렸음!! 순서 주의
    n = n//b
    if r >= 10:
        r= chr(r+55)
    a+=str(r)
print(a[::-1])