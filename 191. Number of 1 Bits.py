def counter_ones(n: int):
    n = list(bin(n))
    res = 0
    for i in n:
        if i == "1":
            res += 1
    print(res)

counter_ones(11)
