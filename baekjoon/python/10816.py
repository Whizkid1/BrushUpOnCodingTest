n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

dic = {}
for i in nl:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in ml:
    if j in dic:
        print(dic[j], end=' ')
    else:
        print(0, end=' ')

# # get 함수를 이렇게 쓸 수 도 있구나...
# def main():
# 	int(input())
# 	card = {}
#
# 	card_input = input().split()
#
# 	for c in card_input:
# 		card[c] = card.get(c, 0) + 1
#
# 	int(input())
#
# 	card2_input = input().split()
#
# 	output = [card.get(c, 0) for c in card2_input]
# 	print(' '.join(map(str, output)))
#
# if __name__ == "__main__":
# 	main()
