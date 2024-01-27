- [generators](#generators)
- [List Comprehension: generators help in this phenomenon](#list-comprehension-generators-help-in-this-phenomenon)
- [Lambda function (anonymous )](#lambda-function-anonymous-)

## generators

specialized code that's able to return a series of values, and to control the iteration process

Iterator: a data type that implements the iterato protocol
`__iter__()` returns the object, invoked only once
`__next__()` returns the next value of the series of values. raises a stop iteration error if there are no more values to provide

The range function is a built in generator

create custom range generator

```python
class CustomRange:
    def __init__(sel, range):
        self.__range = range
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.__i
        self.__i += 1

        if self.__i > self.__range:
            raise StopIteration

        return res

obj_range = CustomRange(10)

for in in obj_range:
    print(i)
```

`yield` keyword:
- pauses the execution until the next time the next method is invoked
- pretty similar to the `return` keyword
- it provides a value but freezes the variable's value until the next invocation

## List Comprehension: generators help in this phenomenon

```python
for i in range(5):
    yield i

first_list = []

for x in range(5):
    first_list.append(10 ** x)

print(first_list)


second_list = [10 ** x for x in range(10)]
print(second_list)


first_list = []

for x in range(5):
    first_list.append(1 if x % 2 == 0 else 0)

print(first_list)


second_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(second_list)

# Replace the square bracets with braces to convert the list comprehension to a generator
```

## Lambda function (anonymous )

A function without a name.
It is useful when working with filter and map methods

```python
sqrt = lambda x: x * x

print(sqrt(2))

add = lambda a, b: a + b
print(add(5 + 3))

```

```python
nums = [1,2,3]
nums_multiplied = list(map(lambda x: x * 3, nums))
print(nums_multiplied)


nums = [1,2,3,4,5,6,7]
nums_even = list(filter(lambda x: x % 2 == 0, nums))
nums_odd = list(filter(lambda x: x % 2 != 0, nums))

print(nums_even, nums_odd)
```

A closure is a technique that allows the storing of values inspite of the fact that the context in which they have been created does not exist anymore.


```python
mix_list = [1, "Python", 0.5, "Apple", 3.0, "\n"]

# create the numbers list using the lambda and filter functions
numbers = list(filter(lambda n: isinstance(n, float) or isinstance(n, int), mix_list))

print(numbers)
```