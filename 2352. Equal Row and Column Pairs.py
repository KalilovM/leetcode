from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    grid2 = []
    for i in range(len(grid)):
        col = []
        for j in range(len(grid)):
            col.append(grid[j][i])
        grid2.append(col)

    f_ind = 0
    s_ind = 0
    res = 0
    while True:
        print(grid[f_ind], grid2[s_ind])

        if grid[f_ind] == grid2[s_ind]:
            res += 1
        s_ind += 1

        if s_ind > len(grid) - 1:
            f_ind += 1
            s_ind = 0

        if f_ind > len(grid) - 1:
            return res


print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
