# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

import math


# Approach 2
def productExceptSelf(nums):
    answer = []
    for i in range(len(nums)):
        cp = nums.copy()
        cp.pop(i)
        answer.append(math.prod(cp))
        i += 1

    return answer


nums = [1, 2, 0, 4]
print(productExceptSelf(nums))


# Approach 2
def productExceptSelfTwo(nums):
    prod = math.prod(nums)
    answer = []
    for i in range(len(nums)):
        if nums[i] != 0:
            answer.append(prod//nums[i])

    return answer


print(productExceptSelfTwo([1, 0, 3, 4]))


# Approach 3
def productExceptSelfThree(nums):
    mul = 1

    for i in nums:
        if i != 0:
            mul *= i

    if 0 in nums:
        if nums.count(0) > 1:
            return [0] * len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = mul
    else:
        for i in range(len(nums)):
            nums[i] = mul//nums[i]

    return nums


print(productExceptSelfThree([1, 0, 3, 4]))
