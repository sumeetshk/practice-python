# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

from itertools import zip_longest


# Approach 1
def mergeAlternately(word1, word2):
    newWord = ''
    lstWord1 = list(word1)
    lstWord2 = list(word2)
    lenWord1 = len(word1)
    lenWord2 = len(word2)

    if lenWord1 < lenWord2:
        lenWord = lenWord1
        longerWord = lstWord2
    else:
        lenWord = lenWord2
        longerWord = lstWord1

    for i in range(0, lenWord):
        newWord += lstWord1[i] + lstWord2[i]

    for i in range(lenWord, len(longerWord)):
        newWord += longerWord[i]

    return newWord


print(mergeAlternately("abc", "pqrst"))


# Approach 2
class Solution:
    def mergeAlternately(self, word1, word2):
        return "".join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]


sol = Solution()
print(sol.mergeAlternately('abc', 'PQR'))


# Approach 3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))


sol = Solution()
print(sol.mergeAlternately('abcd', 'PQRST'))
