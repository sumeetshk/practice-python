class ObjCounter:
    __counter = 0  # private variable 'counter' here

    def __init__(self, val=1):
        self.__first = val  # set a private property 'first' to val
        ObjCounter.__counter += 1  # add here the counter


object_1 = ObjCounter()
object_2 = ObjCounter(2)
object_3 = ObjCounter(4)

print("Object_2 first: ", object_2._ObjCounter__first)
print("Object_3 first: ", object_3._ObjCounter__first)

print("We have created", end=" ")
print(object_3._ObjCounter__counter, "objects")

print("Counter inside the ObjCounter is now", end=" ")
print(ObjCounter.__dict__["_ObjCounter__counter"])
