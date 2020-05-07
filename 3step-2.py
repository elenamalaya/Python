print('Данные для регистрации:')
"""
    name = input("Введите Имя: ")
    surname = input("Введите Фамилию: ")
    year = input("Введите год рождения: ")
    city = input("Введите город рождения: ")
    email = input("Введите Ваш e-mail: ")
    tel = input("Введите Ваш номер телефона 9(999)999-99-99: ")
"""
def my_reg(name, surname, year, city, email, tel):
    return ' '.join([name, surname, year, city, email, tel])

print(my_reg(surname='Malaya', name='Elena', year='2020', city='Samara', email='elena@mail.ru',
              tel='9(999)999-99-99'))
