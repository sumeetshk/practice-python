# running sum
# Approach 1
def fn_running_sum_1(nums):
    list_of_sum = [nums[0]]
    for i in range(1, len(nums)):
        list_of_sum.append(nums[i] + list_of_sum[i - 1])
    return list_of_sum


# Approach 2
def fn_running_sum_2(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


# Approach 3
def fn_running_sum_3(list):
    runSum = [nums[0]]
    for i in range(1, len(nums)):
        runSum.append(runSum[i - 1] + nums[i])
    print(runSum)


nums = [1, 2, 3, 4, 5, 6]
print(fn_running_sum_1(nums))
print(fn_running_sum_2(nums))

nums = [1, 2, 3, 4, 5, 6]
fn_running_sum_3(nums)
