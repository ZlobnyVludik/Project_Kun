# Создание базового класса "Животное" и его наследование для создания классов
# "Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
# и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
# такие как "гавкать" и "мурлыкать".

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} дышит.")

    def eat(self):
        print(f"{self.name} питается.")


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} гавкает.")


class Cat(Animal):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def purr(self):
        print(f"{self.name} мурлычет.")


dog = Dog("Рекс", "овчарка")
cat = Cat("Марсик", "рыжий")

dog.breathe()
dog.eat()

cat.breathe()
cat.eat()

dog.bark()
cat.purr()

print(f"Порода собаки - {dog.breed}.")
print(f"Окрас кошки - {cat.color}.")

