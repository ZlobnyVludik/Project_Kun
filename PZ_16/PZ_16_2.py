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
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} гавкает: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def purr(self):
        print(f"{self.name} мурлычет: Мур-мур!")


# Создание объектов
dog = Dog("Бобик", "Овчарка")
cat = Cat("Мурка", "Рыжий")

# Методы базового класса
dog.breathe()
dog.eat()

cat.breathe()
cat.eat()

# Уникальные методы
dog.bark()
cat.purr()
