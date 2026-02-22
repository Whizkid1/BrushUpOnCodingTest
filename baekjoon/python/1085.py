x,y,w,h = map(int, input().split())
eca = []
eca.append(x)
eca.append(y)
eca.append(w-x)
eca.append(h-y)
print(min(eca))