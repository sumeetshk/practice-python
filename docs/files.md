- [Stream:](#stream)
- [I/O Operations](#io-operations)

## Stream:

- we need to work with sreams to deal with files.
- open - connects to a stream in order to open a file in r, w or rw mode
- close - closes the connection to the stream
- Types:
  - Text - a sequence of typographical caharacters(letters, digits etc)
  - Binary - a sequence of bytes
- When we open a file, Python creates a specific class based on the way that you've opened a file either in r, w or rw mode
- the class exposes some methods that you can use to interact with the stream
- this class is removed when we close the connection
- IOBase
  - RawIOBase
  - BufferedIOBase
  - TextIOBase

```python
stream = open("/path/to/file", "r")
```

## I/O Operations

- sys.stdin: responsible for reading data by the runing program. Ex - input()
- sys.stdout: responsible for outputting data by the running program. Ex - print()
- sys.stderr: responsible for errors raised by runnig program

files processed in Python:

- By writing or reading from a stream saved in memory
- Once a file is accessed with open(), it becomes an object

The built-in function `open()` has a number of parameters. Some of them default to:

- The read mode
- The text mode

```python
f = open("file.txt", "w")
f.close()

# It deletes the file contents if the file already exists
# It creates the file file.txt if it does not exist
```

```python
# open a video file
vf = open("video.mkv", "rb")
video = bytearray(vf.read(100)) # up to 100 bytes

# read a video file
vf = open("video.mp4", 'rb')
buffer = bytearray(1024)
readin = vf.readinto(buffer)
```

```python
from os import strerror


def lipogram(letter):
    letter.lower()
    # Write a try/except block to open the oulipo file
    # use the absolute path /root/code/oulipo.txt
    # and handle an IOError
    try:
        txt = open("/root/code/oulip.txt", "r")
    except IOError as e:
        # print the error with the use of strerror and errno
        print("IO Error: ", strerror(e.errno))
        txt = None
    except Exception as e:
        print(e)
    else:
        # Do the count here using sum(), map(), lambda
        # to count occurences of the letter
        count = sum(map(lambda x: 1 if letter in x else 0, txt))
        print(letter, "appears", count, "times")
    finally:
        if txt:
            txt.close()


lipogram("E")
```
