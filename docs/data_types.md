# Data Types

Python has the following data types built-in by default, in these categories:

- Text Type: str
- Numeric Types: int, float, complex
- Sequence Types: list, tuple, range
- Mapping Type: dict
- Set Types: set, frozenset
- Boolean Type: bool
- Binary Types: bytes, bytearray, memoryview
- None Type: NoneType

## Sequence and Mapping Data Types

| **Dictionary**                         | **Set**               | **List**          | **Tuple**          |
| -------------------------------------- | --------------------- | ----------------- | ------------------ |
| Ordered, mutable                       | Unordered, Immutable  | Ordered, Mutable  | Ordered, Immutable |
| no duplicates                          | no duplicate          | allows duplicate  | allows duplicate   |
| items are presented in key-value pairs | items are not indexed | items are indexed | items are indexed  |

```python
# Examples:

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

myset = {"apple", "banana", "cherry"}

mylist = ["apple", "banana", "cherry"]

mytuple = ("apple", "banana", "cherry")
```
