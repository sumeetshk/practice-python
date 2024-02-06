class Calculator:
    base_value = 10

    def add(self, first_value, second_value):
        print(self.base_value + first_value + second_value)


calc = Calculator()
print(calc.add(1, 2))
