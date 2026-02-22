d = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
w = input()
r = 0
for i in w:
    a = 0
    for j in d:
        a += 1
        if i in j:
            r += (a+2)
print(r)

# 이렇게도 가능하고 더빠르구나...
# str = input()
# ans = 0
# alpabet=[3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
# for s in str:
#     ans += alpabet[ord(s)-ord("A")]
# print(ans)
