
# def my_func():
#     print('Eldi Super!')
#
# my_func()

# def my_func(name):
#    print(f'My name is {name}')
#
# my_func('Eldi')

# def add(num1, num2):
#     print(num1 + num2)
#
# add(15, 2)

# def add(num1, num2, num3):
#     result = num1 + num2 + num3
#     return result
#
# print(add(10, 20, 30 ))
# result1 = add(4, 6, 7)
# print(result1)

# def rectangle(a, b):
#     # a = float(input("Ширина: "))
#     # b = float(input("Высота: "))
#     print("Площадь: %.2f" % (a * b))
#
# def triangle():
#     a = float(input("Основание: "))
#     h = float(input("Высота: "))
#     print("Площадь: %.2f" % (0.5 * a * h))
#
# def circle():
#     r = float(input("Радиус: "))
#     print("Площадь: %.2f" % (3.14 * r ** 2))
#
# rectangle(10, 5)


# def add(q, w, e, r, t, y, u, i, o, p):
#     return q + w + e + r + t + y + u + i + o + p
#
# print(add(1,1,2,3,4,5,56,6,67,7))

# def add(*args):
#     result = 0
#     for i in args:
#         # result = result + 1
#         result += i
#     return result
#
# nums = list(range(20))
# print(add(1,5,3,4,8,6,1,4,2,4,8,7,8,9,5,4,6,1))

# num = 100
#
# def my_func():
#     num = 200
#     print(200)
#
# my_func()
# print(num)

# def add(x, y):
#     return x + y
# print(add(12, 85))
# print(add('asd', '6594'))

# list1 = [1, 4, 5, 6, 7, 9, 98, 14]
# print(sum(list1))

# def func(x):
#     return x * 2
#
# print(func(1) * func('2'))


# def is_year_leap(year):
#     if year % 4  != 0:
#         print('Обычный')
#     elif year % 100 == 0:
#         if year % 400 == 0:
#             print(f'{year} год Високосный')
#         else:
#             print('Обычный')
#     else:
#         print(f'{year} год Високосный')
#
# is_year_leap(int(input('Введите год: ')))


# import time
# # def short_story():
# #     print("У попа была собака, он ее любил.")
# #     print("Она съела кусок мяса, он ее убил,")
# #     print("В землю закопал и надпись написал:")
# #     # time.sleep(1)
# #     short_story()
# #
# #
# # short_story()

# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         print(n)
#         return n * factorial(n -1)
#
# print(factorial(997))

# from datetime import datetime
# start1 = datetime.now()
#
# list_ = []
# for i in range(2000000):
#     list_.append(i)
# # print(list_)
#
# stop1 = datetime.now()
# start2 = datetime.now()
#
# list1 = [i for i in range(2000000)]
# # print(list1)
# stop2 = datetime.now()
#
# print(f"res1 = {stop1 - start1}")
# print(f"res2 {stop2 - start2}")



# def add(x, y):
#     return x + y
#
# lambda_func = lambda x, y: x + y
#
# print(add(2, 3))
# print(lambda_func(2, 3))

# old_list = ['1', '2', '3', '4', '5', '6']
# new_list = list(map(int, old_list))
# print(new_list)

# def func_upper(word):
#     return word.upper()
#
# list_ = list('hello eldi')
# print(list_)
#
# new_list = list(map(func_upper, list_))
# print(new_list)

# mixed = ['мак', 'просо', 'мак', 'просо', 'просо', 'мак', 'мак']
#
# zolushka = list(filter(lambda x: x == 'мак', mixed))
# print(zolushka)

# list_ =  [i for i in range(100)]
# my_func = lambda x: x % 2 ==0
# even_numbers = list(filter(my_func, list_))
# print(list_)
# print(even_numbers)

# from functools import reduce
# list_ = [i for i in range(100)]
# my_func = lambda x, y: x * y
# sum_all = reduce(my_func, list_)
# print(sum_all)

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = 'qwertyui'
# c = (None, True, False, None, True, False)
# res = dict(zip(a, b))
# print(res)


# capitals = tuple(zip(['Russia', 'Kyrgizstan', 'USA'], ('Moscow', 'Bishkek', 'Washington')))
# print(capitals)
