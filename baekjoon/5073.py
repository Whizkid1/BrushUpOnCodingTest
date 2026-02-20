while 1:
    tril = list(map(int, input().split()))
    tril.sort()
    if tril[0] == 0:
        break
    else:
        f, s, t = tril[0], tril[1], tril[2]
        if t >= (f+s):
            print('Invalid')
        elif f == s == t :
            print('Equilateral')
        elif f == s or s == t:
            print('Isosceles')
        else:
            print('Scalene')