input_arr = [str(input()) for _ in range(5)]
max_len = len(max(input_arr, key= lambda x : len(x)))
result = [""] * max_len
for a in input_arr:
    l = len(a)
    i = 0
    for s in a:
        result[i] += s
        i += 1
        if i == l:
            break
print(*result, sep='')
