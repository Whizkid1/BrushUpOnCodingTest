calp=["c=","c-","dz=","d-","lj","nj","s=","z="]
s=str(input())
cnt=0
for i in calp:
    if i in s:
        cnt+=s.count(i)
        s=s.replace(i," ")
print(cnt+len(s.replace(" ", "")))

# 아 좀 더 창의적으로 생각해볼껄
# cro = ["c=",'c-',"dz=","d-","lj","nj","s=","z="]
#
# a = input()
#
# for i in cro:
#     a = a.replace(i,"*")
# print(len(a))