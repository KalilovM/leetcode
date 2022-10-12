def largestPerimeter(nums: list[int]) -> int:
    perimeters = [0]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            for k in range(len(nums)):
                perimeter = 0
                if k == j or k == i:
                    continue
                is_exists = nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] \
                            and nums[j] + nums[k] > nums[i]
                if is_exists:
                    perimeter = nums[i] + nums[j] + nums[k]
                perimeters.append(perimeter)

    return max(perimeters)


print(largestPerimeter([3,2,3,4]))
