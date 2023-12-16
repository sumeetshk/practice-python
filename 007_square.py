###
# Square every element of a list
###


# Approach 1 - Using simple for loop
def fn_square_1(lst_old):
    lst_new = []
    for num in lst_old:  # gets value
        lst_new.append(num ** 2)
    print(lst_new)


lst = [1, 2, 3, 4, 5]
fn_square_1(lst)


# Approach 2 - Modifyung the original list
def fn_square_2(lst):
    for i in range(0, len(lst)):  # gets index
        lst[i] = (lst[i] ** 2)
    print(lst)


lst = [1, 2, 3, 4, 5]
fn_square_2(lst)


# Approach 3 - List Comprehension
def fn_square_3(lst_old):
    lst_new = [num ** 2 for num in lst_old]
    print(lst_new)


lst = [1, 2, 3, 4, 5]
fn_square_3(lst)


# Approach 4 - Using map function
def fn_square_4(num):
    return num ** 2


lst = [1, 2, 3, 4, 5]
lst_new = list(map(fn_square_4, lst))
print(lst_new)


# Approach 5 - Using lambda and map function
lst = [1, 2, 3, 4, 5]
lst_new = list(map(lambda num: num ** 2, lst))
print(lst_new)
