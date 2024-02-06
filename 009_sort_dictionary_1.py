# Dictionary Sorting
from collections import OrderedDict


# Sort Dictionary By Key
def fn_sort_1(dict):
    myKeys = list(dict.keys())
    myKeys.sort()
    sorted_dict = {i: dict[i] for i in myKeys}
    print(sorted_dict, "\n")


# Sort by Keys using collections module:OrderedDict
def fn_sort_2(dict):
    sorted_dict = OrderedDict(sorted(dict.items()))
    print(sorted_dict, "\n")


# Sorting the Keys and Values in Alphabetical Order using the Key
def fn_sort_3(dict):
    for i in sorted(dict):
        print(i, dict[i], end="\n")


# main function
def main():
    myDict = {'h': 1, 'b': 2, 'z': 3, 'e': 5, 'd': 4, 'f': 7, 'g': 1}
    fn_sort_1(myDict)
    fn_sort_2(myDict)
    fn_sort_3(myDict)


# Main function calling
if __name__ == "__main__":
    main()
