import sys
input = sys.stdin.readline

# # 1, 2차 시도 -> 메모리 초과
# # print 도 메모리를 먹는다 해서 했지만 실패... -> 리스트의 메모리를 좀 더 효율적으로 쓰라는 것 같음
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
#
# l.sort()
# # for _ in l:
# #     print(_)
# sys.stdout.write('\n'.join(str(x) for x in l) + '\n')

n = int(input())
c = [0 for _ in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline())
    c[num] += 1

for i in range(10001):
    if c[i] != 0:
        for _ in range(c[i]):
            print(i)