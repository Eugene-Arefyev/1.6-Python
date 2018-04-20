
class Fauna:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def print_info(self):
        print(self.name)
        print(self.size)


class Animal(Fauna):
    def __init__(self, name, size, hoofs):
        super().__init__(name, size)  # super это конструктор родителя
        self.hoofs = hoofs

    def print_info(self):
        super().print_info()
        print(hoofs)


class Birds(Fauna):
    def __init__(self, name, size, color):
        super().__init__(name, size)  # super это конструктор родителя
        self.color = color

    def print_info(self):
        super().print_info()
        print(self.color)


class Cow(Animal):
    def __init__(self, name, size, hoofs, milk_count):
        super().__init__(name, size, hoofs)

        self.milk_count = milk_count

    def print_info(self):
        super().print_info()
        print(self.milk_count)


c = Cow()
