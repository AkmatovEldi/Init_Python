# set_ = {1, 2, 3, 4}
# print(type(set_))
# set2 = set()
# set2 = {1, 2, 3, 4, 1, 2, 3, 4}
# print(set2)
# list_ = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 8, 7, 6, 4]
# list_ = set(list_)
# print(list_)
# set_ = {}
# print(type(set_))
# set_ = {1,7,3,6,9,2,8,0,2,1, 'abc', 'csa, asddas'}
# print(set_)
# print(len(set_))

# add() undate() добавляют элементы в множество
# set_.add(123215)
# print(set_)
# set_.update(set2)
# print(set_)

# discard() remove() удаление элементов множества
# set_ = {1, 3, 6, 10, 15, 21, 28, 36, 45}
# set_.discard(10)
# print(set_)
# set_.remove(0)
# print(set_)
# print(set_.pop())

# union( сложение множеств
#
# set_a = {1, 2, 3, 4, }
# set_b = {4, 5, 6, 7}
# set_c = set_a.union(set_b)
# print(set_c)


# method intersection() (пересечение) возвращает новое множество,содержащее
# все элементы, которые есть и в первом множестве
# set_a = {1, 2, 63, 4, 5 }
# set_b = (4, 5, 2, 63, 5}
# set_c = set_a.intersection(set_b)
# print(set_c)

# method difference() (разность) возвращает новое
# множество, содержащее все элементы, которые есть в множестве
# a_set, но которых нет в множестве b_set.

# set_a = {1, 2, 63, 4, 5 }
# set_b = {4, 5, 2, 63, 88, 5}
# set_c = set_a.difference(set_b)
# print(set_c)

# boolean

# point = input('Введите вашу оценку: ')
# if point == '5':
#     print('Молодец')
# elif point == '4':
#     print('Хорошо')
# elif point == '3':
#     print('Старайся учиться лучше')
# elif point <= '2':
#     print('Старайся учиться лучше')
# elif point <= '2':
#     print('Старайся учиться лучше')
# else:
#     print('Ты можешь лучше!')

# a = int(input('Input number: '))
# b = int(input('Input number: '))

# if a % 10 == 0 or b % 10 == 0:
#     print('Одно из чисел делится на 10 без остатка')
# else:
#     print('Ошибка!!!')


# list_ = [1, 2, 3, 4, 5]
# if 5 in list_:
#     print('5in list')
# if 10 in list_:
#     print('10 in list')
# else:
#     print('10 not in list')
#
# text = 'i like python'
# if 'like' in text:
#     print('word "like" in text')
# if 'hello' not in text:
#     print(text)



# range_ = int(input('input range: '))
#
# for i in range(range_):
#     print(i)
#
# for i in range(20):
#     print(text, str(i))
#     if i == 10:
#         print('break')
#         break
#     print (f'шаг {i}')


# import time
# i = 0
# while True:
#     print('True')
#     time.sleep(1)
#     i = i + 1
#     print(i)