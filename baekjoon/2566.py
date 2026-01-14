arr = [list(map(int, input().split())) for _ in range(9)]
maxx = max([max(i) for i in arr])
r, c = 0, 0
for i in range(9) :
    for j in range(9) :
        if arr[i][j]==maxx:
            r = i+1
            c = j+1
print(maxx)
print(r, c)

# 9*9 형식이 고정된 방식을 역이용
# 9*9 배열을 1차원 배열로 구성 후 find max 후 9로 나눠 r, c를 search

# world = []
#
# for _ in range(9):
#     world += map(int, input().split(" "))
#
# IDX = world.index(max(world))
# print(max(world))
# print(IDX//9+1, IDX%9+1)