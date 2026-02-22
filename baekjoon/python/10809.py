_="abcdefghijklmnopqrstuvwxyz"
q=str(input())
ansl=[]
for i in _:
    ans=q.find(i) #발견된 첫번째 인자 반환해 줌
    ansl.append(ans)
print(*ansl)

# # 아스키로 풀 것 같더니만
# s = str(input())
# for i in range(26) : # 알파벳 개수
#     print(s.find(chr(97+i)), end = ' ') #소문자 알파벳 시작점(아스키)