# Program to check if a given string is Palindrome

# Approach 1
def palindrome(str):
    mid = len(str)//2
    start = 0
    last = len(str) - 1
    flag = 0
    while (start <= mid):
        if (str[start] == str[last]):
            start += 1
            last -= 1
        else:
            flag = 1
            break
    if flag == 0:
        print("Is Palindrome")
    else:
        print("Not Palindrome")


palindrome("abcbaaa")


# Program to check if a given string is Symmetrical
def symmetry(arg):
    n = len(arg)

    if n % 2 == 0:
        mid = n//2
    else:
        mid = n//2 + 1

    start = 0
    flag = 0

    while (start < mid and mid < n):
        if (arg[start] == arg[mid]):
            start += 1
            mid += 1
        else:
            flag = 1
            break
    if flag == 0:
        print("Symmetrical")
    else:
        print("Not Symmetrical")


symmetry("abcab")


# Approach 2
def fn_check_palindrome_and_symmetry(str):
    print("Approach #2")
    half = int(len(str) / 2)
    first_half = str[:half]
    if len(str) % 2:
        second_half = str[half+1:]
    else:
        second_half = str[half:]

    if first_half == second_half:
        print("Symmetric")
    else:
        print("Not Symmetric")

    if first_half == second_half[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


str = input("Enter a string to validate: ")
fn_check_palindrome_and_symmetry(str)
