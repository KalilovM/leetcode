def avarage(salary: list[int]):
    result = (sum(salary)-(max(salary)+min(salary)))/(len(salary)-2)

    print(result)



avarage([1000,2000,3000])
