import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pd = {}
for i in range(1, n+1):
    p = input().rstrip()
    pd[p] = i
dp = {v:k for k,v in pd.items()}
for _ in range(m):
    t = input().rstrip()
    try:
        idx = int(t)
        print(dp[idx])
    except:
        print(pd[t])

# # dict 형태를 유도하는 문제의 예측이 맞았다.
# # -> value로는 key를 찾으려면 다 뒤져야 한다 --=> 그래서 뒤집어진 Dict도 만들었다.
# https://blog.naver.com/wideeyed/222007663089
# # --==> 다른 풀이에는 pd, dp 를 하나에 dict에 담는다...
# # --> 이름은 그냥 리스트를 사용하는 풀이법도 있
# # 또한 try except 가 아닌 숫자를 확인하는 함수를 사용
# import sys
#
# input = sys.stdin.read
#
#
# def main():
#     data = input().splitlines()
#
#     # Divide inputs into pokemon list and problems
#     num_poke, num_q = map(int, data[0].split())
#     pokemons = data[1 : num_poke + 1]
#
#     # Create a dictionary for quick name to index lookup
#     poke_dict = {name: idx + 1 for idx, name in enumerate(pokemons)}
#
#     output = []
#     for q in data[num_poke + 1 :]:
#         if q.isdigit():  # Pokemon Idx?
#             output.append(pokemons[int(q) - 1])
#         else:  # Pokemon Name?
#             output.append(str(poke_dict[q]))
#
#     # Print all results at once to minimize I/O operations
#     sys.stdout.write("\n".join(output) + "\n")
#
#
# if __name__ == "__main__":
#     main()
