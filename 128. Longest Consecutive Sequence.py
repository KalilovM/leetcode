from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = sorted(nums)
    fi = 1
    li = 0
    count = 0
    prevcount = 0
    while True:
        # print(fi, li, count)

        if fi == len(nums):
            return count

        if abs(nums[li] - nums[fi]) == 1:
            count += 1

        else:
            if count > prevcount:
                prevcount = count
                count = 0
        print(abs(nums[li] - nums[fi]))

        li += 1
        fi += 1


print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
