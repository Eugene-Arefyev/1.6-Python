# # 1.7-Python  ООП
# # !!!Объектно - ориентированное програмирование
# # парадигма програмирования(совокупность понятий и идей), в которой основными концепциями являются понятия объектов и классов
#
#
# # !!!Класс(car) это способ описания сущности , определяющий состояние и поведение, зависящее от этого состояния, а также правила для взаимодействия с данной сущностью
# # Это некая абстракция.
#
# # !!!Объект(polo_red, bmw_black, mini, beetle)
# # Это отдельный представитель класса, имеющий конкретное состояние и поведение, полностью определяемое классом
# # это не абстракция, это реальный объектов
#
# # !!!метод - это функция или процедура , принедлежащая какому-то классу или объекту
# # !!!атрибут/поля - переменная связанная с классом или бъектом
#
# # !!!интерфейс(панель приборов) - это набор класса, доступных для использования
# #                                 то как можно взаимодействовать с данной сущностью
#
# # !!!Абстрагирование - это способ выделить набор значимых характеристик объекта, исключая из рассмотрения незначимые
#
# # !!!Инкапсуляция - это свойство системы, позволяющее объеденить данные и методы, работающие с Ними, в классе и скрыть детали реализации от пользователя
# #                   (скрываем детали реализации от пользователя)
#
#
# # !!!Наследование - это свойство системы, позволяющее описать новый класс на основе уже существующего с частично или полностью заимствованной функциональностью
#
# # !!!Полиморфизм - это свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта
#
#
# # Необходимо реализовать классы животных на ферме:
#
# # Коровы, козы, овцы, свиньи;
# # Утки, куры, гуси.
# # Условия:
#
# # Должен быть один базовый класс, который наследуют все остальные животные.
# # Базовый класс должен определять общие характеристики и интерфейс.
class Fauna:
    def __init__(self, name, size):  # __init__ инициализатор класса
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


class Bird(Fauna):
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


class Goat(Animal):
    def __init__(self, name, size, hoofs, horns):
        super().__init__(name, size, hoofs)
        self.milk_count = horns

    def print_info(self):
        super().print_info()
        print(self.horns)


class Sheep(Animal):
    def __init__(self, name, size, hoofs, wool):
        super().__init__(name, size, hoofs)

        self.wool = wool

    def print_info(self):
        super().print_info()
        print(self.wool)


class Pig(Animal):
    def __init__(self, name, size, hoofs):
        super().__init__(name, size, hoofs)

        self.hoofs = hoofs

    def print_info(self):
        super().print_info()
        print(self.hoofs)


class Duck(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size, color)
        self.color = color

    def print_info(self):
        super().print_info()
        print(self.color)


class Chicken(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size, color)
        self.color = color

    def print_info(self):
        super().print_info()
        print(self.color)


class Geese(Bird):
    def __init__(self, name, size, color, long_neck):
        super().__init__(name, size, color)
        self.long_neck = long_neck

    def print_info(self):
        super().print_info()
        print(self.long_neck)


duck = Duck("Утя", 456, "white")
geese = Geese("Гусыня", 12, "bleack", "long_neck")
chiken = Chicken("Цыпа", 77, "red")

cow = Cow("бурёнка", 12, 4, 5)
sheep = Sheep("бебе", 21, 4, 'wool')
pig = Pig('naf-naf', 44, 4)
goat = Goat('meme', 32, 4, 2)
