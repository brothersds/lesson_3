'''
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод
данных о пользователе одной строкой.
'''


def my_func(name, surname, year_birth, current_city, user_email, phone_number):
    return print(f"name - {name}; surname - {surname}; year_birth - {year_birth}; current_city - {current_city}; user_email - {user_email}; phone_number - {phone_number}")


my_func(name=Ivan, surname=Petrov, year_birth=1956, current_city=Moscow, user_email=sds@mail.ru, phone_number=2113636)
