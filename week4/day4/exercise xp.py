#ex1
# def display_message():
#     print("i want chicken and waffles")
# display_message()

#ex2
# def favourite_book(title):
#     print("One of my favourite books is" + title)
# favourite_book(title = " Alice in wonderland")
#

#ex3
# def describe_city(city, country):
#     print(city + " is in " + country)
# describe_city(city="Kyoto", country="Japan")

#ex4
# import random
# def guess():
#    num=int(input("Enter a number from 1 to 100"))
#    print(num)
#    range=random.randrange(1,100)
#    print(int(range))
#
#    if num != range:
#        print("You lost")
#    else:
#        print("You win!")
# guess()

#ex5
# 123
# def make_shirt(shirt, text):
#     print(" size of shirt " + shirt + " , with message " + text)
#
# make_shirt(shirt= "small",text="nada")
# #4
# def make_shirt(shirt=" large ", text=" i love python"):
#     print(" shirt size: " + shirt + " with message " + text)
#

#5
# def make_shirt(shirt , text=" i love Python "):
#     print("Shirt of size: " + shirt+ " and with message: " + text)
# make_shirt("Medium")
# make_shirt("Large")
# make_shirt("Small","Vitamin Sea")
#     #6/
# def make_shirt(**kwargs):
#         print(kwargs)
#     make_shirt(size='Small', text="Get 'em!")


# ex6
# magician_names=["Apolla","Houdini","Blaine","Copperfield"]
# # def show_magicians():
# #     for i in magician_names:
# #         print("One of the magician is: "+i)
# # show_magicians()
#
# def show_magicians():
#     for i in magician_names:
#         print("One of the magician is: "+i)
#     def make_great():
#         for i in magician_names:
#             print("One of the magician is: "+ f"the Great {i}")
#     make_great()
# show_magicians()
