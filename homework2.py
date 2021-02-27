# task 1 +++
# a = [1, 2, 2, 4, 11, 2, 3, 1]
# set1 = set(a)
# a = list(set1)
# print(a)

# task 2 +++
# a = ['John', 'Anna', 'Raychel', 'Katarina', 'Marko', 'Tom']
# del a[5], a[4], a[0]
# print(a)

# task 3 +++
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num.reverse()
# # num.sort(reverse=True)
# # num.sort(reverse=-1)
# print(num)

# task 4 +++
# students = ['Eldi', 'Erik', 'Damira', 'Azamat']
# print(students)
# students[1] ='Kauhar'
# print(students)

# task 5 +++
# text = input('Введите слова через пробел: ')
# list1 = text.split()
# list1.sort(key=len)
# print(list1)


# task 6 +++
# phone = {'iPhone': '12proMax', 'Samsung': 'A51', 'Xiomi': 'Note5'}
# key = input('Введите ключ: ')
# if phone.get(key):
#     print(f'Ключ {key} есть в словаре')
# else:
#     print('Такого ключа нет в словаре')

# task 7 +++
# car = {'Mers': 212, 'BMW': 'M5'}
# bike = {'yamaha': 300, 'suzuki': 'sport'}
# car.update(bike)
# print(car)

# task 8 ---
dict1 = {1: 'a', 3: 'c', 2: 'b', 4: 'd'}
a = list(dict1.keys())
a.sort()
for i in a:
    print(i, ':', dict1.get())

# task 9 +++
# car = {}
# bike = {'yamaha': 300, 'suzuki': 'sport'}
# 2 варианта
    # if bike:
    #     print(f'Словарь: {bike}')
    # else:
    #     print('Словарь пуст!')
# if len(car) == 0:
#     print('Словарь пуст!')
# else:
#     print(f'Словарь: {car}')

# task 10 +++
# list1 = [25, 85, 95, 74, 54]
# list1.append(84)
# list1.insert(0, 'Eldi')
# list1.append('python')
# print(list1)
# list1 = tuple(list1)
# print(list1)

# task 11 +++
# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# dictionary = dict([(login, password)])
# print(dictionary)

# task 12 +++
# letter = input('Введите букву: ')
# vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# vowelseng = ['a', 'e', 'i', 'o', 'u', 'y']
# if letter.isalpha():
#     if letter in vowels or letter in vowelseng:
#         print(f'Буква {letter} гласная')
#     else:
#         print(f'Буква {letter} согласная')
# else:
#     print('Ошибка! Нужно ввести букву!')

# task 13 +++
# apple = int(input('Введите кол-во яблок: '))
# students = int(input('Введите кол-во студентов: '))
# if apple >= students:
#     res = apple - students
#     print(f'{students} студентов получили по яблоку, в корзине осталось {res} яблок!')
# elif apple < students:
#     print('Студентов больше чем яблок, яблоки в корзине!')

# task 14 +++
# apprentice = int(input('Введите кол-во учеников: '))
# if apprentice % 2 == 0:
#     desks = apprentice / 2
#     print(f'{int(desks)} нужно для класса')
# else:
#     desks = apprentice // 2 + 1
#     print(f'{desks} нужно для класса')

# task 15 +++
# agedog = int(input('Введите возраст собаки: '))
# sizedog = int(input('Введите размер собаки 1-Большой 2-Средний 3-Маленький: '))
# if sizedog == 1:
#     humanage = agedog * 12.5
#     print(f'Возраст вашей большой собаки: {humanage}')
# elif sizedog == 2:
#     humanage = agedog * 10.5
#     print(f'Возраст вашей средней собаки: {humanage}')
# elif sizedog == 3:
#     humanage = agedog * 9
#     print(f'Возраст вашей маленькой собаки: {humanage}')
# else:
#     print('Введите цифру от 1 до 3')

# task 16 +++
# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# c = int(input('Введите число: '))
# if a > 10 and b > 10 and c > 10:
#     print(f'Все три числа больше 10: {a}, {b}, {c}')
# else:
#     print('No')

# task 17 +++
# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# c = int(input('Введите число: '))
# l = [a, b, c]
# amount = 0
# i = 0
# for i in l:
#     if i > 0:
#         amount += 1
# print(f'Положительных чисел {amount}')

# task 18 +++
# num = int(input('Введите целое число: '))
# step = int(input('Введите множитель: '))
# result = 0
# if num < 100:
#    result = num ** step
#    print(result)
# else:
#     print('Введенное вами число > 100')

# task 19 +++
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# m = 0
# if a > m:
#     m = a
# if b > m:
#     m = b
# if c > m:
#     m = c
# print(m)

# task 20 +++
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# if a > b and a < c or a < b and a > c:
#     print(f'Число а является средним: {a}')
# elif b > a  and b < c or b < a and b > c:
#     print(f'Число b является средним: {b}')
# # else:
# #     print(f'Число c является средним: {c}')
# elif c > a  and c < b or c < a and c > b:
#     print(f'Число c является средним: {c}')
# else:
#     print('Введите 3 разных числа!')
