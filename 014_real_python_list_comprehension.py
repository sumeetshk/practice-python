lst = [2, 3, 4, 5, 6]


# Method 1
def square(x):
    return x * x


result_1 = list(map(square, lst))
print(result_1)


# Method 2
result_2 = []
for num in lst:
    result_2.append(square(num))

print(result_2)


# Method 3 - Pythonic
result_3 = [square(num) for num in lst]
print(result_3)


# Print odd item in the list
def is_odd(x):
    return x % 2 == 1


result_odd = list(filter(is_odd, lst))
print(result_odd)
