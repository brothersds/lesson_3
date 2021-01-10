'''
Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.
'''

quit_task = False


def my_func_summ(*args):
    global quit_task
    my_data = args[0]
    my_summ = 0
    for index in my_data:
        try:
            if 'Q' in index:
                quit_task = True
                return my_summ
            elif 'q' in index:
                quit_task = True
                return my_summ
            my_summ += int(index)
        except ValueError:
            continue
    return my_summ


user_summ = 0
while not quit_task:
    user_list = input('Для выхода нажмите Q\nВведите числа, разделенных пробелами: ').split()
    user_summ += my_func_summ(user_list)
    print(f'Сумма чисел равна: {user_summ}')
    continue
print('end')
