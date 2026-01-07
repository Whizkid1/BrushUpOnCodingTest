f, s = map(str, input().split())
f = int(f[::-1])
s = int(s[::-1])
if f > s:
    print(f)
else:
    print(s)