# Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол".
# Напишите метод, который выводит информацию о человеке в формате
# "Имя: имя, Возраст: возраст, Пол: пол".

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}.")

person = Human("Иван", 25, "мужской")
person.show_info()
