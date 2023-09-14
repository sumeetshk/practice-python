###
# Find if a number is prime
###
import math

num = int(input("Enter a number: "))


# Approach 1 - using flag
# Time complexity: O(sqrt(n))
# Auxiliary space: O(1)
def fn_prime_1(num):
    if num > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime == True:
            print(str(num) + ' is Prime')
        else:
            print(str(num) + ' is Not Prime')
    else:
        print(str(num) + " is Neither")


# Approach 2
def fn_prime_2(num):
    if num == 1:
        print(str(num) + " is Neither")
    for i in range(2, (num // 2) + 1):
        if (num % i) == 0:
            print(str(num) + " is Not Prime")
            break
    else:
        print(str(num) + " is Prime")


# Approach 3 - using recursion
# Time complexity: O(sqrt(n))
# Auxiliary space: O(sqrt(n))
def fn_prime_3(num, itr):
    if itr == 1:
        return True  # base condition
    if num % itr == 0:
        return False  # if given num is divided by itr or not
    if fn_prime_3(num, itr - 1) == False:
        return False
    return True


itr = int(math.sqrt(num)+1)


# Function Calls
fn_prime_1(num)
fn_prime_2(num)

if fn_prime_3(num, itr):
    print(str(num) + " is Prime")
else:
    print(str(num) + " is Not Prime")
