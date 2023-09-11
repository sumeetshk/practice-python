###
# Find max of 2 numbers
###

# Approach 1
def fn_max_1():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd Number: "))
    print('Maximum is:' + str(max(a, b)) + '\n')


fn_max_1()


# Approach 2
def fn_max_2(a, b):
    if a >= b:
        return a
    else:
        return b


a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
print('Maximum is ' + str(fn_max_2(a, b)))
