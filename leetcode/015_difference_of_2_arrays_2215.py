# 2215. Find the Difference of Two Arrays

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]

# Approach 1
def findDifferenceOne(nums1, nums2):
    ans = []
    ans.append(list(set(nums1) - set(nums2)))
    ans.append(list(set(nums2) - set(nums1)))
    return ans


# Approach 2
def findDifferenceTwo(nums1, nums2):
    ans1 = []
    ans2 = []
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))

    for i in range(len(nums1)):
        if nums1[i] not in nums2:
            ans1.append(nums1[i])

    for j in range(len(nums2)):
        if nums2[j] not in nums1:
            ans2.append(nums2[j])

    return ans1, ans2


# Test
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

print(findDifferenceOne(nums1, nums2))
print(findDifferenceTwo(nums1, nums2))
