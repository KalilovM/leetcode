def subtractProductAndSum(n: int) -> int:
    prod = 1
    sum = 0
    n = str(n)
    for i in n:
        prod *= int(i)
        sum += int(i)

    return prod - sum


print(subtractProductAndSum(4421))
