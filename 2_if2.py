"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(a, b):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not isinstance(a, str) or not isinstance(b, str):
        return 0 
    elif a == b:
        return 1
    elif a != b and b == 'learn':
        return 3
    elif len(a) > len(b):
        return 2

    
    
if __name__ == "__main__":
    print(main(1, 2))
    print(main('Python', 'Python'))
    print(main('PythonPython', 'Python'))
    print(main('Python', 'learn'))
