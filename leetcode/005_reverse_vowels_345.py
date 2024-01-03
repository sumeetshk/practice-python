# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Approach 1
def reverseVowelsOne(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_in_string = []
    s = list(s)
    j = 0
    for i in range(len(s)):
        if s[i] in vowels:
            vowels_in_string.append(s[i])

    vowels_in_string.reverse()

    for i in range(len(s)):
        if j < len(vowels_in_string):
            if s[i] in vowels:
                s[i] = vowels_in_string[j]
                j += 1

    return "".join(s)


print(reverseVowelsOne('hello'))


# Approach 2
def reverseVowelsTwo(s):
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1

        # Swap the vowels at the left and right positions
        s_list[left], s_list[right] = s_list[right], s_list[left]

        left += 1
        right -= 1

    return ''.join(s_list)


print(reverseVowelsTwo('LEETCODE'))
