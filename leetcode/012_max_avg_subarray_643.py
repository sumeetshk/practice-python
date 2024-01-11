# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.

def findMaxAverage(nums, k):

    currSum = maxSum = sum(nums[:k])

    for i in range(k, len(nums)):

        currSum = currSum - nums[i - k] + nums[i]

        maxSum = max(maxSum, currSum)

    return maxSum / k


n = [1, 12, -5, -6, 50, 3]
print(findMaxAverage(n, 3))


# Alternate Approach
# for i in range(0, len(nums) - k):
#     currSum -= nums[i] + nums[i+k]
#     maxSum = max(maxSum, currSum)
