# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time


def func_log(file_log='log.txt'):
    """
    Декоратор дозаписывает в файл имя вызываемой функции (получаемый по атрибуту __name__), дату и время вызова функции
    :param file_log: путь до файла
    :return:
    """
    def funcs(func):
        def wrapper():
            today = datetime.datetime.today()
            func()
            with open(file_log, "a", encoding="utf-8") as file:
                func_time = f"{func.__name__} вызвана %d.%m %H:%M:%S\n"
                file.write(today.strftime(func_time))

        return wrapper
    return funcs


@func_log()
def func1():
    time.sleep(3)


@func_log(file_log="func2.txt")
def func2():
    time.sleep(5)


func1()
func2()
func1()
