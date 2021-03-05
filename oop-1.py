# class Person:
#     money = 100
#
# user = Person
# print(user.money)


# class Person:
#     name = ''
#     money = 0
#
#
# person1 = Person()
# person2 = Person()
#
# person1.name = 'Eldi'
# person2.name = 'Damira'
#
# person1.money = 100
# person2.money = 50
# print(person1.name, person1.money)
# print(person2.name, person2.money)


# class Person:
#     name = ''
#     money = 0
#
#     def about(self):
#         print(f'{self.name} has {self.money}')
#     def change_money(self, new_money):
#         self.money = new_money
#
#
#

# class Critter:
#     total = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Critter.total += 1
#         print(f'PПоявилось новое животное {name}')
#
#     def talk(self):
#         print(f'hello. My name is {self.name}')
#
#     @staticmethod
#     def status():
#         print(f'Сейчас всего {Critter.total} животных')
#
# pet = Critter('Barbosso', 6)
# pet = Critter('Morzos', 4)
# pet.talk()
# Critter.status()


# class A:
#     def _private(self):
#         print('This is private method')
#
# a = A()
# a._private()
#
#
# class B:
#     def __closed__(self):
#         print('This is closed metod')
#
#     def print_close(self):
#         self.__closed()
#         print('closed method is working')
#
#
#
# b = B()
# b.print_close()


# class MyList(list):
#     def append(self):
#         print('Это не тот append что у класса list')
#
# list1 = MyList()
#
# list1.append(10)
# list.insert(0, 1)
# list.insert(1, 2)
# list.insert(2, 3)
#
# print(list1)
# print(type(list1))


class Dog:
    total = 0

    def __init__(self, name, age, hunger=0):
        self.name = name
        self.age = age
        self.hunger = hunger
        Dog.total +=1
        print(f'created new object of class Dog')
        print(f'total objects of class {Dog.total}')

    def __pass_time(self):
        self.hunger += 1

    def talk(self):
        print(f'My name is {self.name}')
        self.__pass_time()

    def eat(self):
        print('Thanks')
        self.hunger -= 2
        self.__pass_time()

    def walk(self):
        print(f'I like to walk')
        self.__pass_time()


dog = Dog('Gray', 2, 3)

class Dachshund(Dog):
