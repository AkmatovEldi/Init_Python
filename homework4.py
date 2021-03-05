# task 1+++
# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# task 2 +++
# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#         i += 1
#     else:
#         i += 1

# task 3 +++
# i = 0
# while i < 1 or i > 10:
#     i = int(input('Введите число от 1 до 10: '))
#
# print(f'Ваше число в диапозоне от 1 до 10: {i}')

parol = 'Eldi'
i = 1
while i != 3:
    pas1 = input('Введите пароль: ')
    if pas1 == parol:
        print('Пароль верный!')
    else:
        i += 1
        print('Повторите ввод!')
print('ПАроль не верный! Вы потратили 3 попытки!')