###
# Swap first and last item of a list
###


# Approach 1
def swapList(list):
    list[0], list[-1] = list[-1], list[0]
    return list


list = list(input("Enter a List: "))
print(swapList(list))


# Approach 2
def swapList_1(list):
    start, *mid, end = list
    list = [end, *mid, start]
    return list


list1 = input("Enter a List: ")
print(swapList_1(list1))
