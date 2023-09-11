###
# Find sum of 'n' natural numbers
###

# Approach 1
def fn_sum_of_n_natural_numbers(num):
    sum = int(num * (num + 1) / 2)
    return sum


n = int(input("Enter Number: "))
s = fn_sum_of_n_natural_numbers(n)
print("Sum of ", n, " natural numbers ", s)
