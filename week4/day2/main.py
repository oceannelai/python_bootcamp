# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


#lists
# a_tuple = (10,20,30,40)
# a,b,c,d = a_tuple
# print(a)
# print(b)
# print(c)
# print(d)



# for loop exercise
# number =int(input("put a number"))
# for i in range(1,13):
#     print(number,"x",i, "=", (i*number))

# while loop exercise
# current_number = 1
# while current_number <= 10:
#     print(current_number)
#     current_number += 1
#
# print("Finished")

#exercise XP

#exercise 1

# my_fav_numbers  = {6,8,29,2,9}
# my_fav_numbers.add(90)
# my_fav_numbers.add(360)
# print(my_fav_numbers)
# my_fav_numbers.remove(9)
# print(my_fav_numbers)
# friend_fav_numbers = {12, 69, 76, 66}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#exercise 2 turple

# it is not possible

#exercise 3 print a range of numbers

# for i in range(1,21):
#     print(i)
#
# #exercise 4 Float
#
# current_number = 1.5
# while current_number <= 5.5 :
#         print(current_number)
#         current_number += 0.5
#
# #exercise 5
#
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("kiwi")
# print(basket)
# basket.insert(0,"Apples")
# print (basket)
# print (basket.count("Apples"))
# print(basket.clear())
#
# #exercise 6 loop
# my_name = " "
# while my_name != 'Oceanne':
#  my_name = input('What is your name?')
#
# print('Congrats we are in the same league!')

#exercise 7
# my_list = ["peach"," Anastasia"," shampoo"," conditioner"," sneakers"];
# for i in range(1,len(my_list),2):
#      print(my_list[i])

#exercise 8

# i=1500
# while i <= 2500:
#     if ( i % 5==0 and i % 7 ==0):
#         print (i)
#     i+=1

#exercise9
# fruits = input("Enter your favourite fruit(s)")
# my_list = fruits.split()
# print(my_list)
#
# fruity = input("Enter any fruit")
#
# if fruity in fruits:
#         print("You chose one of your favorite fruits! Enjoy!")
# else:
#         print("You chose a new fruit. I hope you enjoy")

#exercise 10

# toppings = input("Choose your topping")
#
# active = True
# while active:
#     adding = input("Topping added, Choose more or quit?")
#     if topping == 'quit':
#         active = False
#print("Your total is:",10+2.5,"for each topping")
#exercise 11
# age=int(input("Enter age or enter '0' to quit:"))
# price = []
# active= True
# while age != 0:
#     age=int(input("Enter age or enter '0' to quit:"))
#     # for i in list:
#     if age <= 3:
#           price.append(0)
#     elif age>3 and age<12:
#           price.append(10)
#     elif age== 0:
#           active = False
#     else:
#           price.append(15)
# print(sum(price))

# # exercise XP 12
# name_list = ['varsh', 'Princess', 'Adrien', 'dylan']
#
# name = input("Enter your name")
# if name in name_list:
#      age= int(input("Enter your age"))
# if age<16 :
#     name_list.remove(name)
#
# print(name_list)

#exercise 13
#finished_sandwiches = []


#ex14


#gold xp
#ex1
# my_list = ["apple","peach","lollipop","kale"]
# list2 = ["broccoli","sandwich","bracelet","rose"]
# two_list = my_list.union(list2)
# print(two_list)

#ex2
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
#
# if (num1 > num2) and (num1 > num3):
#     largest = num1
# elif (num2 > num1) and (num2 > num3):
#     largest = num2
# else:
#     largest = num3
#
#print("The largest number is", largest)


#ex3
# l = input("abcdefghijklmnopqrstuvwxyz")
#
# if l in ('a', 'e', 'i', 'o', 'u'):
# 	print("%s is a vowel." % l)
# elif l == 'y':
# 	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
# else:
#	print("%s is a consonant." % l)



#daily challenge
# from datetime import datetime, timedelta
# """" Taking input from user and converting it to datetime object"""
# birthday = input("what is your birthday? ex.DD/MM/YY")
# birthday_convert_to_date = datetime.strptime(birthday, "%d/%m/%y")
# """ Specifing the current"""
# current_date =datetime.now()
# """ age"""
# age = int((current_data.year - birthday_convert_to_date)/365/timedelta)
# age_to_string =str(age)
# last_digit_age = int(age_to_string[-1])
# candles = "i" * 5
