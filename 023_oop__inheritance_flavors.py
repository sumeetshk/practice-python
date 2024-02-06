class Desert:
    def __init__(self, flavor):
        self.flavor = flavor


class IceCream(Desert):
    def __init__(self, flavor):
        super().__init__(flavor)

    # Add a custom string representation
    def __str__(self):
        return "My favorite flavor is " + self.flavor


# Create an object IceCream with a pistachio flavor
obj = IceCream("pistachio")

print(obj)


###

class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)
