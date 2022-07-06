I i, [6/7/22 10:40]
#ПОЛИМОРФИЗМ
# принцип ООП в котором меттоды в разных классах называются одинаково(1 интерфейс ,разный функционал)
class Dog:
    def speal(self):
        print('gaf gaf gaf')
class Cat:
    def speal(self):
        print('mow mow mow')
class Frog:
    def speal(self):
        print('kwa kwa kwa')
animals = [Cat(), Dog(), Dog(), Frog()]
for animal in animals:
    animal.speal()
# print(dir(list))
# print(dir(str))
# print(dir(dict))
print(dir(int))