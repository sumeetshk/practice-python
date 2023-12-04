# Exceptions

- 63 built in exceptions in tree hierarchy
- if you want to handle 2 or more exceptions the same way add the names into comma separated list
- errors can also be raised inside functions
- errors can be handled either inside or outside the function as demonstrated below:

```python
# try block inside function
def calculate_user_input():
	try:
		x = int(input('Enter a Number: '))
		y = 1 / x
		print(y)
	except(ZeroDivisionError, ValueError):
		print("Invalid Input Value")
	except(Arithmetic Error):
		print("CalculationFailed")
	except:
		print("Something Else went wrong")

	return None

calculate_user_input()

# try block outside function
def calculate_user_input():
	x = int(input('Enter a Number: '))
	y = 1 / x
	print(y)

	return None

try:
	calculate_user_input()
except(ZeroDivisionError, ValueError):
	print("Invalid Input Value")
except(Arithmetic Error):
	print("CalculationFailed")
except:
	print("Something Else went wrong")

```

## raise

manually raise an excepotion

## assert
raises an AssertionError if the expression evaluates to a falsy value
useful if we want to be absolutely safe from the wrong data if you are not sure if the dat ahas been carefully examined beforehand

```python
import math

x = int(input("Enter a number: "))
assert x >= 0

x = math.sqrt(x)
print("Result: ", x)

```

Abstract Exception - general exception that include other exceptions