# ex1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Persian (Cat):
#     def sing(self,sounds):
#         return f'{sounds}'
#
# my_cats = [Bengal(" Yasaar ", 2),Chartreux(" Varsh ",5),Persian(" Gigi ", 3)]
# my_pets = Pets(my_cats)
#
# my_pets.walk()


#2
class Dog():
    def __init__(self,name, age, weight):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
    def bark (self):
        print(f'{self.name} is barking')

    def run_speed(self):
        return int(self.weight/self.age*10)
        print  (int(self.weight / self.age * 10))
    def fight (self,other_dog):
        self.other_dog = other_dog
        if int(self.run_speed()) * int(self.weight) > int(other_dog.run_speed()) * int(other_dog.weight):
           print(f'{self.name} has won!')
        else:
           print(f'{other_dog.name} has won!')

mi_pero1 = Dog("Rex", 3,10)
mi_pero2 = Dog("Juan",2,12)
mi_pero3 = Dog("waffy", 1,9)
mi_pero1.fight(mi_pero2)





