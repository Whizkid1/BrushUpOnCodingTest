# fail...
s=str(input())
a=0
for i in set(s):
    il=list(filter(lambda x: s[x] == i, range(len(s))))
    if len(il)>1:
        for j in range(0,len(il)-1):
            f=il[j]
            n=il[j+1]

# answer.....
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)

