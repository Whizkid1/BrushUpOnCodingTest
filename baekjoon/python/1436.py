n = int(input())
cnt = 0
pop = 0
while 1:
    pop += 1
    if '666' in str(pop): # 여기서 '666' 위치가 중요하다!
        cnt += 1
    if cnt == n:
        break
print(pop)
