###
# Find Runner-up Score
###

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])

    print(sorted(set(arr), reverse=True)[1])


def fn_runner_up(n, list):
    new_arr = [num for num in list if num != n]
    return new_arr


arr = list(arr)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(sorted(set(arr), reverse=True)[1])
