def fizzbuzz(numbers):
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = "fizzbuzz"
    return numbers


nums = [45, 22, 14, 65, 97, 72]
fizzed_num = fizzbuzz(nums)
print(fizzed_num)


def fizzbuzz_1(numbers):
    for i, num in enumerate(numbers):
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = "fizzbuzz"
    return numbers


nums = [45, 22, 14, 65, 97, 72]
print(enumerate(nums))
fizzed_num = fizzbuzz_1(nums)
print(fizzed_num)
