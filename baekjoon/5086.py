while 1:
    f, s = map(int, input().split())
    if f == 0:
        break
    if f <= s:
        if s % f == 0:
            print("factor")
        else:
            print("neither")
    else:
        if f % s == 0:
            print("multiple")
        else:
            print("neither")