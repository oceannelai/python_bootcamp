# people =["rick","beth","morthy","jerry","snowball"]
# people_filter = list(filter(lambda people :len(people) <=4,people))
# print(people_filter)


# exercises xp
# 1
# class Cat():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.felines={}
#     def cats(self,cat_name,cat_age):
#         self.felines[cat_name]= cat_age
#
# type_of_cat = Cat("Feline",1)
# type_of_cat.cats("kitty", 7)
# type_of_cat.cats("garfield", 12)
# type_of_cat.cats("paw", 3)
# # print(type_of_cat.felines)
# print(dict(sorted(type_of_cat.felines.items(),key=lambda item:[1])))
# keys = list(type_of_cat.felines.keys())
# print(type_of_cat.felines[list(type_of_cat.felines.keys()[-1])])


#2

# class Dog():
#     def __init__(self,name,height):
#         self.name =name
#         self.height =int(height)
#     def bark(self):
#         print(f"{self.name} woof")
#     def jump(self):
#         print(f"{self.name} jumps " + f"{self.height *2} cm height ")
#
# davids_dog = Dog("Rex",58)
# davids_dog.jump()
# sarahs_dog =Dog("teacup",20)
# sarahs_dog.bark()
# sarahs_dog.jump()
#
# jump_height = [davids_dog.height,sarahs_dog.height]
# for i in jump_height:
#         if davids_dog.height > sarahs_dog.height:
#             print(f"{davids_dog.name} is bigger")
#         else:
#             print(f"{sarahs_dog.name} is bigger")
#

# 3
class song():
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def  sing_me_a_song(self): :
        print(f"{self.lyrics} you love me")



