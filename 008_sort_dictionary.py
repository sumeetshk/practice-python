# Dictionary Sorting
# Displaying the Keys in sorted order
def fn_sort_1(key_val):
    for i in sorted(key_val.keys()):
        print(i, end="\n")


# Keys and Values sorted in alphabetical order by the VALUE
def fn_sort_2(key_val):
    print(sorted(key_val.items(), key=lambda kv: (kv[1], kv[0])))


def main():
    key_value_pair = {}

    key_value_pair[2] = 56
    key_value_pair[4] = 27
    key_value_pair[5] = 67
    key_value_pair[6] = 9
    key_value_pair[1] = 33
    key_value_pair[3] = 83

    # Print the original KeyValue Pair
    print("key_value", key_value_pair, "\n")

    fn_sort_1(key_value_pair)

    fn_sort_2(key_value_pair)


if __name__ == "__main__":
    main()
