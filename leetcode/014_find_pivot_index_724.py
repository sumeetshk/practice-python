# 724. Find Pivot Index

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of
# the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because
# there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndexOne(nums):
    sumLeft = 0
    sumRight = sum(nums)

    for i in range(0, len(nums)):

        sumRight -= nums[i]

        if i == 0:
            sumLeft = 0
        else:
            sumLeft += nums[i-1]

        if sumLeft == sumRight:
            return i

    return -1


def pivotIndexTwo(nums):
    for i in range(0, len(nums)):
        if sum(nums[0:i]) == sum(nums[i+1:]):
            return i
    return -1


# Test
nums = [1, 7, 3, 6, 5, 6]
# nums = [1,5,6,5,1]
# nums = [2,0,0]

print(pivotIndexOne(nums))
print(pivotIndexTwo(nums))
