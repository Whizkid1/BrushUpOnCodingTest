a, b, c, d, e, f = map(int, input().split())
def search_xy(a, b, c, d, e, f):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a*x + b*y) == c and (d*x + e*y) == f:
                return x, y
print(*search_xy(a, b, c, d, e, f))

# 엉...?
# a,b,c,d,e,f=map(int,input().split())
# x=(c*e-b*f)//(a*e-b*d)
# y=(c*d-a*f)//(b*d-a*e)
# print(x,y)