# Pushing into and Popping from a stack

# Procedural Approach
stackList = []


def push(val):
    stackList.append(val)


def pop():
    val = stackList[-1]
    del stackList[-1]
    return val


push(4)
push(5)

print(pop())
print(pop())


# OOPS Approach
class Stack:
    def __init__(self):  # constructor function
        self.__stackList = []  # prefix __ to make the variable private, refer encapsulation

    # push function
    def push(self, val):
        self.__stackList.append(val)
        # print(self.stackList)

    # pop function
    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


# class invocation to create object
my_stack = Stack()

# call push function using object
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# call pop function using object and print the popped value
print(my_stack.pop())
my_stack.pop()
print(my_stack.pop())


# create another object by invokin class
my_stack_2 = Stack()

my_stack_2.push('A')
my_stack_2.push('B')
my_stack_2.push('C')

print(my_stack_2.pop())
