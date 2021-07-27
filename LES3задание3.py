#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a1 , a2, a3):
    if a1 >= a3 and a2 >= a3:
        return a1 + a2
    elif a1 > a2 and a1 < a3:
        return a1 + a3
    else:
        return a2 + a3

print(f'результат - {my_func(int(input("введите аргумент 1")), int(input("введите аргумент 2")), int(input("введите аргумент 3")))}')