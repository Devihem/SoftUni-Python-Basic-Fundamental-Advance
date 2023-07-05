from project.animals.birds import Owl, Hen
from project.animals.animal import Animal
from project.food import *
from project.animals.mammals import Dog

dog1 = Dog("Murdjo", 10, 'Varna')
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(10)
print(dog1)
print(dog1.make_sound())
dog1.feed(veg)
print(dog1.feed(fruit))
dog1.feed(meat)
print(dog1)
