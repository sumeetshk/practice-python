# 1431. Kids With the Greatest Number of Candies

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that you have. Return a boolean array result of length n, where result[i] is
# true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.


# Approach 1
def kidsWithCandiesOne(candies, extraCandies):
    result = []
    for i in range(len(candies)):
        total = candies[i] + extraCandies
        if total >= max(candies):
            result.append(True)
        else:
            result.append(False)

    return result


# Approach 2
def kidsWithCandiesTwo(candies, extraCandies):
    return [i + extraCandies >= max(candies) for i in candies]


# Approach 3
def kidsWithCandiesThree(candies, extraCandies):
    result = []
    for i in candies:
        total = i + extraCandies
        result.append(total >= max(candies))

    return result


# Test Data
candies = [5, 3, 6, 1]
extraCandies = 3


# Run
print(kidsWithCandiesOne(candies, extraCandies))
print(kidsWithCandiesTwo(candies, extraCandies))
print(kidsWithCandiesThree(candies, extraCandies))
