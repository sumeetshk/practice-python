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


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))


# Approach 2
def productExceptSelfTwo(nums):
    prod = math.prod(nums)
    answer = []
    for i in range(len(nums)):
        answer.append(prod//nums[i])

    return answer


print(productExceptSelfTwo([1, 2, 3, 4]))
