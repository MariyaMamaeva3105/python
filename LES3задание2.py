#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input('имя')
surname = input('фамилия')
year = int(input('возраст'))
city = input('город')
email = input('email')
telephone = int(input('телефон'))

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print("Меня зоавут: ", name, "Моя фамилия: ", surname, "Мой возраст: ", year, "Мой город: ", city, "Мой email: ", email, "Мой номер телефона", telephone, sep=',')
