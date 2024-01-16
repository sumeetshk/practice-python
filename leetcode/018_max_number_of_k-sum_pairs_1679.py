# 1679. Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.


# Approach
# Sort the array: We begin by sorting the input array nums. Sorting is essential for the two-pointer approach. using the nums.sort()

# Iterate with two pointers: Use a while loop to iterate until left pointer is less than right pointer.
# - If the sum of nums[left] and nums[right] is equal to the target k, we have found a pair,
# so we increment the operation count and move both pointers towards the center
# - If the sum is less than k, we need a larger sum, so we move the left pointer to the right.
# - If the sum is greater than k, we need a smaller sum, so we move the right pointer to the left.

# Return the count: After the while loop completes, return the operation count,
# which represents the maximum number of pairs that can be formed to achieve the target sum.


def maxOperations(nums, k):
    left = 0
    right = len(nums) - 1
    count = 0

    nums.sort()

    while left < right:
        sum = nums[left] + nums[right]
        if sum == k:
            count += 1
            left += 1
            right -= 1
        elif sum < k:
            left += 1
        else:
            right -= 1

    return count


# Test
nums = [3, 1, 3, 4, 3, 2]
k = 6

print("count: ", maxOperations(nums, k))
