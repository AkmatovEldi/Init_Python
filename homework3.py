
# task 1 +++
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for i in a:
#     if i < 5:
#         b.append(i)
# print(f'Выведены все числа которые меньше 5: {b}')

# task 2 +++
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# 1вариант работает только без вложенных списков
# # c =  list(set(a) & set(b))
# c = []
# 2 вариант (вложенные циклы)
# for i in a:
#     if i in c:
#         continue
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

# task 3 +++
# python = {1: 'Eldi', 2: 'Ainur', 3: 'Nursultan', 4: 'Akyl', 5: 'Syimyk'}
# java = {6: 'Erik', 7: 'Urmat', 8: 'Borya'}
# go = {9: 'Ulan', 10: 'Almaz'}
# # python.update(java)
# # python.update(go)
# merge = {**python, **java, **go}
# print(merge)

# task 4 +++
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217
# ]
#
# for i in numbers:
#     if i % 2 == 0 and i != 237:
#         print(i)

# task 5 +++
# a = int(input('Введите 1-ое число: '))
# b = int(input('Введите 2-ое число: '))
# if a == b:
#     print("Введите разные числа")
# elif a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(b, a + 1):
#         print(i)

# task 6 +++
# num1 = int(input('Введите минимальное число: '))
# num2 = int(input('Введите максимальное число: '))
# for i in range(num1, num2):
#     if i * i < num2:
#         res = i * i
#         print(res)

# task 7 +++
# list1 = [1, 2, 6, 3, 9, 2, 11, 20, 16, 7, 8]
# even = 0
# odd = 0
# for i in list1:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print(f'Четных чисел: {even}')
# print(f'Нечетных чисел: {odd}')

# task 8 +++
# num = int(input('Введите число: '))
# for i in range(num + 1):
#     i = str(i) * i
#     print(i)

# task 9 +++
# num = int(input('Введите число от 1 до 10: '))
# for i in range(1, 11):
#     res = num * i
#     print(f'{num} * {i} = {res}')

# task 10 +++
# min = int(input('Введите минимальное число: '))
# max = int(input('Введите максимальное число: '))
# step = int(input('Введите шаг: '))
# list1 = []
# for i in range(min, max + 1, step):
#     list1.append(i)
# print(list1)

# task 11 +++
# num_fib = int(input('Введите число: '))
# list1 = []
# nas = 0
# pred1 = 1
# pred2 = 0
# # list1.append(pred1)
# for i in range(num_fib):
#     nas = pred2 + pred1
#     list1.append(nas)
#     pred2 = pred1
#     pred1 = nas
#     i = i + 1
# print(list1)

# task 12 +++
#  1 вариант
# import math
# num = int(input('Введите число: '))
# fact1 = math.factorial(num)
# print(f'Факториал числа {num}! = {fact1}')
# 2 вариант
# num = int(input('Введите число: '))
# fact1 = 1
# if num > 0:
#     for i in range(1, num + 1):
#         fact1 *= i
# else:
#     print('Введите число больше 0!')
#
# print(f'Факториал числа {num}! = {fact1}')
