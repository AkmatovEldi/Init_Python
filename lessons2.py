list_ = [1, 2, 3, 4, 5, 6]
list2 = [1, 'eldi', [1, 2, 3], (1, 2,3 )]
# print(type(list2))
# print(len(list_))
# text = 'hello eldi'
# print(text[0])
# print(text[-1])
# print(text[-5])
# print(text[0:4])
# print(text[:8:2])
# print(text[::-1])
# print(text[-1] + text[-2])
# print(list2[-+1])
# print(len(list2))
# print(list2[2][2])
# print(list2[2][-1])


# method append

# list1 = [1, 2, 3, 4, 5, 6]
# list1.append(10)
# print(list1)
# list1.append('new element')
# print(list1)


# method extend расширяет список другим списком

# list1 = [1, 2, 3, 4]
# list2 = [0, 9, 8, 7]
# list1.extend(list2)
# print(list1)
# print(list1 + list2)


# method insert добавляет поиндексно элемент имеет 2 аргумента

# cars = ['mersedes', 'honda', 'subaru']
# cars.insert(0, 'tesla')
# print(cars)

# method remove удаляет эдемент из списка по значению

# cars.remove('honda')
# print(cars)


# method pop вырезает из списка элемент, который можно сохранить

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# last_element = list1.pop(4)
# list1.pop(6)
# print(list1)
# print(last_element)

# method index выводит индекс эл-та

# students = ['Eldi', 'Erkin', 'Azat', 'Erik']
# print(students.index('Azat'))


# method count подсчитывает кол-во элементов по заданному аргументу

# print(students.count('Eldi'))
# print(len(students))


# method reverse разворачивает список

# students.reverse()
# print(students)


# method sort сортирует список по умолчанию
# students = [1, 2, 8, 6, 7, 1, 8, 40, 64, 84,]
# students.sort(key=len, reverse=True)
# students.sort()
# print(students)


# method clear

num = [1, 2, 8, 6, 7, 1, 8, 40, 64, 84,]
# num.clear()
# print(num)
del num[5]
print(num)


# diapazon = list(range(0, 25, 5))
# print(diapazon)

# TUPLE - КОРТЕЖ

# new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 5, 6, 7,2, 4, 8, 7, 1, 4)
# new_tuple2 = tuple()
# print(type(new_tuple))
# print(new_tuple.count(1))
# print(new_tuple.index(2))


# dictionary - словари

# dict1 = {}
# dict2 = dict()
# capitals = {'Moscow': 'Russia', 'Bishkek': 'Kyrgizstan', 'Kiev': 'Ukraine'}
# print(capitals)
# print(len(capitals))


# method fromkeys

# dictionary = dict.fromkeys(['key1', 'key2'], 'value')
# print(dictionary)


# method get() получает по ключу значение

# capitals = {'Moscow': 'Russia', 'Bishkek': 'Kyrgizstan', 'Kiev': 'Ukraine'}
# print(capitals.get('Bishkek'))

# method keys выводит все ключи
# print(capitals.keys())

# method values выводит все значения
# print(capitals.values())
# print(capitals['Moscow'])
# print(capitals['Almaty'])

# method items() возвращает пары (ключ+значение)

# pairs = capitals.items()
# print(pairs)

# method pop удаляет пару и возвращает значение
# val = capitals.pop('Moscow')
# print(val)
# print(capitals)

# method popitem
# last_pair = capitals.popitem()
# print(type(last_pair))
# print(capitals)

# method update
# capitals2 = {'Washington': 'USA', 'Paris': 'France'}
# capitals.update(capitals2)
# print(capitals)

#


