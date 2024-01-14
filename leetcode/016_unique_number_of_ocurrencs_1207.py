# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

def uniqueOccurrencesOne(arr):
    from collections import Counter
    c = Counter(arr)
    return len(c) == len({c[x] for x in c})


# Approach 2
# Create a map to store the frequency of each element in the array.
# Create a set to store the unique number of occurrences.
# Iterate over the map and check if the number of occurrences of any element is already present in the set.
# If it is present, return false.
# Otherwise, add the number of occurrences to the set.
# Return true.

def uniqueOccurrencesTwo(arr):
    count_occ = {}
    occ_set = set()
    for each_num in arr:
        if each_num not in count_occ:
            count_occ[each_num] = 1
        else:
            count_occ[each_num] += 1

    for num, count in count_occ.items():
        if count in occ_set:
            return False
        else:
            occ_set.add(count)

    return True


# Approach 3
# Use the Counter class from the collections module to count the occurrences of each element in the array.
# Maintain a set to store the counts.
# Iterate through the counts obtained from the Counter and check if each count is already present in the set. If yes, return False, indicating non-unique counts. Otherwise, add the count to the set.
# If the iteration completes without returning False, return True, indicating that all counts are unique.

def uniqueOccurrencesThree(arr):
    data = Counter(arr)
    counts = set()
    for value in data.values():
        if value in counts:
            return False
        counts.add(value)
    return True


arr = [1, 2, 2, 1, 1, 3]
print(uniqueOccurrencesOne(arr))
print(uniqueOccurrencesTwo(arr))
print(uniqueOccurrencesThree(arr))
