# 2390. Removing Stars From a String

# You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"

def removeStars(s):
    ans = []
    for i in s:
        if i == '*':
            ans.pop()
        else:
            ans.append(i)
    return "".join(ans)


# Test
s = "leet**cod*e"
print(removeStars(s))
