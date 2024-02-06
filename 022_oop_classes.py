# issubclass and isinstance methods

class One:
    pass


class Two(One):
    pass


class Three(Two):
    pass


issubclass(One, One)   # returns True
issubclass(Three, One) # returns True
issubclass(Two, One)   # returns True

one = One()
two = Two()

isinstance(two, Two)  # returns True
isinstance(one, One)  # returns True
isinstance(two, One)  # returns True
