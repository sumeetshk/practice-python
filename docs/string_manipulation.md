- [String Manipulation](#string-manipulation)
  - [Standards](#standards)
  - [Methods](#methods)

# String Manipulation

String is an immutable sequence of data:

- It can be treated as lists in many cases
- we can index and slice strings
- we cannot use `del` or `append` as its immutable

## Standards

1. ASCII uses 8 bits - first 128 standard alphabets
2. Code Pages - first 128 code points can make different characters in different code pages,
   - helped ininternalization for a while
   - designed for western european languages
3. Unicode - assigned unique characters to more than a million code points
   - UTF 8 - Unicode Transformation Format
   - uses one to four 1byte code units

## Methods

- len: length of string
- ord: returns codepoint
- chr: returns codepoints corresponding to the character
- min: returns min value of the sequence
- max: returns max value of the sequence
- index: returns provided character's index
- count: returns the sum of all occurrences of the provided character
- list: creates a new list containing all the string characters
- capitalize:
- center: returns new string padded with the provided characters
  ```python
  print('Hello'.center(9, '*'))
  **Hello**
  ```
- endswith: checks if a string ends with certain characters
- startswith: checks if a string starts with certain characters
- find: returns index of the first occurrence of the provided character, returns -1 if not found
- rfind: returns index of the last occurrence of the provided character
- isalnum: checks if a string only contains alphanumeric value
- isalpha: checks if a string only contains letters
- isdigit: checks if a string only contains digits
- islower: checks if all the chars in a string are lowercase
- isupper: returns true if all the characters in the string are uppercase
- isspace: returns true if all the characters in a string are whitespace
- join: returns a single string based on the list elements and delimiter
  ```python
  $ print('-'.join(['abc', 'def', 'ghi']))
  abc-def-ghi
  ```
- split: returns a list based on the string element and delimiter
  ```python
  print('abc--def--ghi'.split('--'))
  ['abc', 'def', 'ghi']
  ```
- lower: returns a string with all lower case letters
- upper: returns a string with all upper case letters
- lstrip: removes leading characters from a string `print('www.kodekloud.com'.lstrip('w.'))`
- rstrip: removes trailing characters from a string `print('www.kodekloud.com'.rstrip('.com'))`
- strip: removes both leading and trailing characters from a string `print('0000123450000'.strip('0'))`
- replace: replaces certain characters in a string with the provied characters
  ```python
  print('That is great'.replace('great', 'awesome'))
  ```
- swapcase: saps the casing of each character
- title: changes the casing of the first character to uppercase, the rest lower case
- sorted: returns a new, sorted list fom a list or string

  ```python
  print(sorted(['kiwi', 'apple', 'mango']))
  ['apple', 'kiwi', 'mango']

  print(sorted('Sort Me!'))
  [' ', '!', 'M', 'S', 'e', 'o', 'r', 't']
  ```

- sort: modifies the list by sorting the elements

  ```python
  fruits  ['kiwi', 'apple', 'mango']
  sorted_fruits = fruits.sort()
  print(fruits)

  # ['apple', 'kiwi', 'mango']
  ```

- str: stringify an element
- int/float: converts a string to an integer/float
-
