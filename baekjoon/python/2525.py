h, m = input().split()
h, m = int(h), int(m)
rm = int(input())
trm = m+rm

if trm >= 60:
    rh = (trm//60)
    m = (trm%60)

    trh = h+rh
    if trh >= 24:
        h = trh - 24
    else:
        h = trh
else:
    m = trm
print(h, m)