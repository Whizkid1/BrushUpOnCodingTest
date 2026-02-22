tril = list(map(int, input().split()))
tril.sort()
f, s, t = tril[0], tril[1], tril[2]
if (f+s) > t:
    print(f+s+t)
else:
    print((f+s)*2-1)