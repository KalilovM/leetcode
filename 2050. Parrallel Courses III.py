from typing import List


def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    dictionary = {}
    for i in range(n):
        dictionary[i] = time[i]

    print(dictionary)


minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5])
