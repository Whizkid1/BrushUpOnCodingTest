f, s, t = input().split()
f, s, t = int(f), int(s), int(t)

if f == s == t:
    print(10000 + f * 1000)
elif f == s or f == t:
    print(1000 + f * 100)
elif s == t:
    print(1000 + s * 100)
else:
    print(max(f, s, t)*100)
