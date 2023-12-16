# Program to reverse an input string

# Approach 1
def fn_reverse_a_string(a):
    n = len(a)
    a_list = list(a)
    b = n-1
    for i in range(int(n/2)):
        a_list[i], a_list[b] = a_list[b], a_list[i]
        b -= 1
        # print(i, b)

    return a_list


a = input("Enter: ")
print(fn_reverse_a_string(a))


# Approach 2
def fn_rev_str():
    arg = "abc def xyz wef"
    arg = arg.split()[::-1]
    print(" ".join(arg))


fn_rev_str()


# Approach 3
def fn_reverse_a_string_3(str):
    reversedString = ""
    for i in str:
        reversedString = i + reversedString
    return reversedString


stringToBeReversed = input("Enter String: ")
reversedString = fn_reverse_a_string_3(stringToBeReversed)
print("Reversed String: ", reversedString)
