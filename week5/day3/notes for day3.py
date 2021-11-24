# #CLASS ATTRIBUTE
# class Dog():
#     dogs_king = "Bernie IV"  #This is a class . Can be private but shouldn't be(if not using decoratores). Otherwise, we won't be able to access it
#
#
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog
#
#     def bark(self):
#         print("{} barks ! WAF".format(self.name))
#
#     def walk(self, number_of_meters):
#         print("{} walked {} meters".format(self.name, number_of_meters))
#
#     def rename(self, new_name):
#         self.name = new_name
#
# my_dog = Dog("Rex")
# my_dog.rename("Paul")
#
# print("The king of the dogs is:", Dog.dogs_king)

#CLASS DECORATORS
# A static method is a method that doesn’t get self.

# class MyClass:
#   @staticmethod
#   def add(a, b):
#     return a + b
#
#
#
# print(MyClass.add(3, 6))
# # >> 9

# # Class methods are methods that are not bound to an object but to a class. Its first argument is the class itself (remember that classes are objects too).
#
# class MyClass:
#   __counter = 0
#
#   @classmethod
#   def add(cls,a):
#     return cls.__counter + a
#
# my_class_add = MyClass.add(3)
# print(my_class_add)
# # >> 3
#
# new_class = MyClass()
# new_class.__counter = 1
#
# print(new_class.add(3))
# # >> 4
#
# # The output is still three because the method add refers to the class definition, not the counter of the new_class instance

# #PROPERTY
# #1. Getter
# # Without @property
#
# class MyClass:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name
#
#   def email(self):
#     return "{}.{}@gmail.com".format(self.first_name,  self.last_name )
#
# newClass = MyClass("John", "Doe")
# print(newClass.email())
# # >> John.Doe@gmail.com
#
# #With property
# class MyClass:
#   def __init__(self, first_name, last_name):
#     self.__first_name = first_name
#     self.__last_name = last_name
#
#   @property
#   def email(self):
#     return "{}.{}@gmail.com".format(self.__first_name,  self.__last_name )
#
# newClass = MyClass("John", "Doe")
#
# print(newClass.email())
# # >> TypeError: 'str' object is not callable
#
# print(newClass.email) #property has to be run without ()
# # >> John.Doe@gmail.com

# #2. Setter
# class MyClass:
#   def __init__(self, first_name, last_name):
#     self.__first_name = first_name
#     self.__last_name = last_name
#
#   @property
#   def email(self):
#     return "{}.{}@gmail.com".format(self.__first_name,  self.__last_name )  #this is the getter
#
#   @email.setter  #this is the setter
#   def email(self, name):
#     self.__first_name = name
#
# newClass = MyClass("John", "Doe")
# newClass.email = "Sarah" #the setter changes the name to Sarah #The '=' sign indicates that we run a function that sets a new value through self.email
# print(newClass.email)
# # >> Sarah.Doe@gmail.com

# class MyClass(object):
#     count = 0
#
#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1
#
#     def set_val(self, newval):
#         self.val = newval
#
#     def get_val(self):
#         return self.val
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count()) #1 appears because it's the first time we accessing something
#
# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())
#
# class MyClass(object):
#     count = 0
#
#     def __init__(self, val):
#         self.val = self.filterint(val)
#         MyClass.count += 1
#
#     @staticmethod
#     def filterint(value):
#         if not isinstance(value, int):
#             print("Entered value is not an INT, value set to 0")
#             return 0
#         else:
#             return value
#
#
# a = MyClass(5)
# b = MyClass(10)
# c = MyClass(15)
#
# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint(100))
#
#