class Animal:
    def __init__(self, type):
        self.type = type


class Mammal(Animal):
    def __init__(self, animal):
        Animal.__init__(self, "mammal")
        self.animal = animal

    def breathe(self):
        print("Breathing...")


class Dog(Mammal):
    def __init__(self, breed):
        super().__init__("dog") # super() can be used instead of superclass name. Withthis, `self` is not required in the init method
        self.breed = breed

    def bark(self):
        print("Woof..")


crocodile = Animal("reptile")

dolphin = Mammal("dolphin")

pet = Dog("Labrador")

print(dolphin.type)
print(dolphin.breathe())

print(pet.type)
print(pet.breathe())
print(pet.bark())

print(isinstance(pet, Dog))
print(isinstance(pet, Animal))
print(isinstance(dolphin, Dog))
print(isinstance(dolphin, Animal))

print(issubclass(Mammal, Animal))
print(issubclass(Animal, Dog))


##############

class SuperA:
	var_a = 10
	def fun_a(self):
		return 11

class SuperB:
	var_b = 20
	def fun_b(self):
		return 21

class Sub(SuperA, SuperB):
	def sub_method(self):
		pass

obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())
