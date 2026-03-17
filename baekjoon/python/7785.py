n = int(input())
s = set()
for _ in range(n):
    name, state = input().split()
    if state == "enter":
        s.add(name)
    else:
        s.remove(name)
print(*sorted(s, reverse=True), sep='\n')