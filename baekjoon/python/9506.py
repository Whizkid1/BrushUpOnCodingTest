while 1:
    n = int(input())
    if n == -1 :
        break
    divisors_list = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            divisors_list.append(i)
            if (i ** 2) != n:
                divisors_list.append(n // i)
    divisors_list.sort()
    divisors_list.pop()
    if n == sum(divisors_list) :
        divisors_list.pop(0)
        answer = f"{n} = 1"
        for i in divisors_list:
            answer += f" + {i}"
        print(answer)
    else: print(f"{n} is NOT perfect.")

