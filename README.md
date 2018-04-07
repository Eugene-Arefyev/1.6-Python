# 1.6-Python
# !!!Объектно - ориентированное програмирование 
# парадигма програмирования(совокупность понятий и идей), в которой основными концепциями являются понятия объектов и классов


# !!!Класс(car) это способ описания сущности , определяющий состояние и поведение, зависящее от этого состояния, а также правила для взаимодействия с данной сущностью
# Это некая абстракция.

# !!!Объект(polo_red, bmw_black, mini, beetle) 
# Это отдельный представитель класса, имеющий конкретное состояние и поведение, полностью определяемое классом
# это не абстракция, это реальный объектов

# !!!метод - это функция или процедура , принедлежащая какому-то классу или объекту
# !!!атрибут/поля - переменная связанная с классом или бъектом

# !!!интерфейс(панель приборов) - это набор класса, доступных для использования
#                                 то как можно взаимодействовать с данной сущностью

# !!!Абстрагирование - это способ выделить набор значимых характеристик объекта, исключая из рассмотрения незначимые

# !!!Инкапсуляция - это свойство системы, позволяющее объеденить данные и методы, работающие с Ними, в классе и скрыть детали реализации от пользователя
#                   (скрываем детали реализации от пользователя)  


# !!!Наследование - это свойство системы, позволяющее описать новый класс на основе уже существующего с частично или полностью заимствованной функциональностью

# !!!Полиморфизм - это свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта


Необходимо реализовать классы животных на ферме:

Коровы, козы, овцы, свиньи;
Утки, куры, гуси.
Условия:

Должен быть один базовый класс, который наследуют все остальные животные.
Базовый класс должен определять общие характеристики и интерфейс.

Создадим общий класс
class Fauna():
    def __init__(self, name, size, paws, hoofs, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.hoofs = hoofs
        self.wings = wings
        print (self.name, self.size, self.paws, self.hoofs, self.wings)

        def info(self):
            print(self.name, self.size, self.paws, self.hoofs, self.wings)

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
            'hoofs': self.hoofs,
            'wings': self.wings,
        })


class Birds(Fauna):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Fauna.__init__(self, name_bird, 'small', 2, 'None', 'Yes')


class Animal(Fauna):
    name_animal = ['Коровы', 'Козы', 'Овцы', 'Свиньи']
    def __init__(self, name_animal):
        self.name_animal = name_animal
        Fauna.__init__(self, name_animal, 'big', 4, 'Yes', 'None')
        
class Cows(Animal):
    def __init__(self, name, size, paws, hoofs, wings):
        super().__init__(name, size, paws, hoofs, wings)
        self.hoofs = 4

    # def horns(self):
    #     self.horns = 4
    #     print("{} имеет {} рога и {} копыта."
    #           .format(self.name, self.horns, self.hooves))

    # def give(self, milk):
    #     self.milk = milk
    #     self.animal_type = '"млекопитающие"'
    #     print("{} относится к типу {} и даёт в среднем {} литров молока "
    #           "в месяц.".format(self.name, self.animal_type, self.milk))


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')

Cows = Animal('Коровы')
Goats = Animal('Козы')
Sheep = Animal('Овцы')
Pigs = Animal('Свиньи')

# print(Birds._dict_)
print('\n Класс Птицы:',
      '\n Утки: {}' .format(ducks),
      '\n Куры: {}' .format(chickens),
      '\n Гуси: {}' .format(geese))

print('\n Класс Животные:',
      '\n Коровы: {}'.format(Cows),
      '\n Козы: {}'.format(Goats),
      '\n Овцы: {}'.format(Sheep),
      '\n Свиньи: {}'.format(Pigs))
