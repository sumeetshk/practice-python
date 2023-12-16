# function to find length fo a string
def fn_length_of_string(string):
    length_count = 0
    for i in string:
        length_count += 1
    return length_count


string = input("Enter String: ")
str_len = fn_length_of_string(string)
print("Length of the string is: ", str_len)
