'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def div_numbers(number_1, number_2):
    return number_1/number_2


user_list = list((input('Введите два числа, разделенных пробелами: \n')).split())

try:
    print(div_numbers(int(user_list[0]), int(user_list[1])))
except ZeroDivisionError:
    print('Деление на ноль!')
print('end program')
