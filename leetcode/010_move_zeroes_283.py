# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Approach 1
def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(0)
    return nums


# Approach 2
class Solution:
    def moveZeroesTwo(self, nums):
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1

        return nums


# Run
nums = [1, 0, 3, 4, 0, 0, 5, 0, 6, 7]

print(moveZeroes(nums))

obj = Solution()
print(obj.moveZeroesTwo(nums))
