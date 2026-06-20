# 1. ИНКАПСУЛЯЦИЯ

class Person:
    def __init__(self):
        self.__age = None  

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным")

    def get_age(self):
        return self.__age


# 2. НАСЛЕДОВАНИЕ

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an Animal"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# 3. ПОЛИМОРФИЗМ

class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()

# 4. АБСТРАКЦИЯ

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

p = Person()
p.set_age(25)
print(p.get_age()) # Вывод: 25*
p.set_age(-5)  #Должна быть ошибка или предупреждение*

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())  # Buddy Woof
print(cat.name, cat.speak())  # Kitty Meow

car = Car()
bike = Bicycle()

print(move(car))   # Car is driving
print(move(bike))  # Bicycle is pedaling

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())   # 50
print(circle.area()) # ~153.86