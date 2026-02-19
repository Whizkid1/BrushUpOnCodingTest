f = int(input())
s = int(input())
t = int(input())

if (f+s+t) != 180:
    print("Error")
elif f == s == t:
    print("Equilateral")
elif (f == s) or (s == t) or (t == f):
    print("Isosceles")
else:
    print("Scalene")