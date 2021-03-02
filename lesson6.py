#
# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print('Ошибка деления на ноль')
#
# print('Код работает дальше')
#
# try:
#     print(1 / 0)
# except Exception as ex:
#     print(ex)
# print('Код работает дальше')

# try:
#     print(1 + 1)
# except Exception as ex:
#     print(ex)
# finally:
#     print('Эта строка работает в любом случае')
# print('Код работает дальше')

# lesson3 = open('lesson3', 'r')
# lesson3.close()

# with open('lesson3', 'r') as file:
#     file.write('lesson3 = open('lesson3.py', 'r')\n')
#     file.write('Эта строка работает в любом случае')
#
# with open('text.txt', 'a') as fileL:
#     fileL.write('new data')

# with open('lesson5.py', 'a') as file:
#     color = ['Red' 'Green', 'Black', 'White', 'Pink', 'Yellow']
#     for i in color:
#         file.write(i + '\n')
#
# with open('lesson5.py', 'r') as file:
#


import os
# os.remove('new')
# os.rename('fa.txt', 'da.txt')
import shutil

# shutil.copyfile('main.py', 'new')


# import random
# random_list = [random.randint(1, 1000) for i in range(1000)]
# random_list.sort()
# random.shuffle(random_list)
# print(random_list)

# list = [i for i in range(50)]
# print(random.choice(list))

# list_ = [33, 5, 14, 89, 22, 41]
# # list_.sort()
# sorted_list = sorted(list_)
# print(sorted_list)
# print(list_)
