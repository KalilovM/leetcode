from typing import List

# import math


def minDifference(nums: List[int], queries: List[List[int]]) -> List[int]:
    array = []
    for i in range(len(queries)):
        a, b = queries[i]
        b += 1
        current = nums[a:b]
        res = 0
        if len(set(current)) == 1:
            array.append(-1)
            continue
        li = 0
        ri = 0
        while True:
            
            
            

        array.append(res)
    return array


print(minDifference([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]))
