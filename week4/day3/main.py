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



#exercise XP
#ex1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# dictionary = dict(zip(keys,values))
# print(dictionary)

#ex2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
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
#
# print(price)
# family_prices=zip(family.keys(),price)
# prices={}
# for i,j in family_prices:
#     prices[i]= j
# print(prices)
# print(sum(price))

#exercise3

# name: "Zara "
# creation_date: 1975
# creator_name:"Amancio Ortega Gaona "
# type_of_clothes: ["men", "women", "children", "home"]
# international_competitors: ["Gap", "H&M", "Benetton"]
# number_stores: 7000
# major_color:{
# "France": "blue",
# "Spain": "red",
# "US": ["pink","green"]
# }
# brand ={"name":["Zara"],
#         "creator_date":[1975],
#         "creator_name":["Amancio Ortega Gaona "],
#         "type_of_clothes":["men", "women", "children", "home"],
#         "international_competitors":["Gap", "H&M", "Benetton"],
#         "number_stores":[7000],
#         "major_color":{"France":"blue","Spain":"red","US":["pink","green"]}}
#
# brand["number_stores"] =2
#
# print("Zara's clients are:",brand["type_of_clothes"][0:3])
# brand["country_creation"]=["spain"]
#
# if "international_competitors" in brand:
#         brand["international_competitors"].append("Desigual")
#
# del brand["creator_date"]
#
# print(brand["international_competitors"][-1])
#
# print(brand["major_color"]["US"])
#
# print(len(brand))
#
# print(brand.keys())
#
# more_on_zara ={"creation_date":[1975],
#                "number_stores":[10000]
#                }
# brand.update(more_on_zara)
# print(brand.values())
# print(brand)

#ex4

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
#1/

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_users_A = {key: i for i , key in enumerate(users)}
print(disney_users_A)

#2/
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_users_B = {}
for(index,val) in enumerate(users):
    disney_users_B[index] = val
    print(disney_users_B)
#3/
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
users.sort()
print(users)
disney_users_C ={ key: i for i,key in enumerate(users)}
print(disney_users_C)

#4

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_users_A= {key: i for i, key in enumerate(users)}
print(disney_users_A)