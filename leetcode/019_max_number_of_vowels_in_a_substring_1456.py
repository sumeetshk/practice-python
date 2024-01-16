
# 1456. Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.


# Approach 1
# Create a list called vowels containing the characters 'a', 'e', 'i', 'o', and 'u'.
# Initialize two variables: max_vowel to keep track of the maximum number of vowels found in any window and curr_vowel to keep track of the current number of vowels in the current window.
# Iterate through the first k characters of the string s (the initial window):
#   Check if each character is in the vowels set.
#   If a character is a vowel, increment curr_vowel.
# Set max_vowel equal to curr_vowel, as this represents the maximum number of vowels in the initial window.
# Continue iterating through the rest of the string from index k to the end:
#   For each iteration, remove the leftmost character of the current window (at index i - k) and check if it's a vowel. If it is, decrement curr_vowel.
#   Add the rightmost character of the current window (at index i) and check if it's a vowel. If it is, increment curr_vowel.
#   Update max_vowel by taking the maximum of curr_vowel and the current max_vowel.
# Finally, return max_vowel, which represents the maximum number of vowels in any substring of length k within the string s.

def maxVowels(s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in range(k):
        if s[i] in vowels:
            count += 1

    max_count = count

    for i in range(k, len(s)):
        if s[i-k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1

        max_count = max(max_count, count)

    return max_count


# Approach 2
def maxVowelsTwo(s, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max = 0
    for i in range(len(s) - k + 1):
        lst_ss = s[i: i+k]
        count = 0
        for j in range(k):
            if lst_ss[j] in vowels:
                count += 1
            if count > max:
                max = count

    return max


# Test
s = "leetcode"
k = 3

print(maxVowels(s, k))
print(maxVowels(s, k))
