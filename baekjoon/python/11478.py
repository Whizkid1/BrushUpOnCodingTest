s = input()
l = len(s)+1
t = len(s)
ss = set()
while t :
    for i in range(l-t):
        print(s[i:t+i])
        ss.add(s[i:t+i])
    t -= 1
print(len(ss))