s=str(input()).upper()
alp=[0]*26
for i in s:
    alp[ord(i)-65] += 1
if alp.count(max(alp)) > 1:
    print("?")
else:
    print(chr(alp.index(max(alp))+65))

# 숏코딩
# s=input().upper();c=s.count;*_,a,b=v=sorted({*s,'?'},key=c);print(v[-(c(a)<c(b))])

# 좀 더 빠른 코드
# word = input().upper()
# word_list = list(set(word))
# lst = []
#
# for i in word_list:
#     cnt = word.count(i)
#     lst.append(cnt)
#
# if lst.count(max(lst)) >= 2:
#     print("?")
# else:
#     print(word_list[lst.index(max(lst))])

# 좀 더 빠른 코드 222
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
#
# a = input()
# a = a.lower()
#
# cnt = []
# for i in alphabet:
#     num = a.count(i)
#     cnt.append(num)
#
# ind = cnt.index(max(cnt))
#
# sort = sorted(cnt, reverse=True)
#
# if sort[0] == sort[1]:
#     print("?")
# else:
#     print(alphabet[ind].upper())