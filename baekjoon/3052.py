s = set()
for _ in range(10):
    t = int(input())
    r = t%42
    s.add(r)
print(len(s))

# 다른 사람의 미친 풀이....
# print(len(set([int(input())%42 for _ in range(10)])))
# print(len({int(i)%42for i in open(0)}))