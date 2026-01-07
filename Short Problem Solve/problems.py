# age = 20
# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenager")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")

#
# userAge = int(input("Enter your age : "))
# enterDay = input("Enter Day :")
# print(enterDay.lower())

# price = 12 if userAge >= 18 else 8

# if str(enterDay.lower()) == "wednesday":
#     price = price - 2

# print("your ticket price is", price)

# second method

# userAge = input("Enter your age :")
# convetInt = int(userAge)
# enterDay = input("Enter Today Day :").strip().lower()
# price = 12
# childPrice = 8
# if convetInt >= 18:
#     if enterDay == "wednesday":
#         price = price - 2
#         print("your ticket price is", price)
#     else:
#         print("your ticket price is", price)
# else:
#     if enterDay == "wednesday":
#         childPrice = childPrice - 2
#         print("your ticket price is", childPrice)
#     else:
#         print("your ticket price is", childPrice)

# third method
# age = int(input("Enter your age :"))
# day = input("Enter today's day :").strip().lower()
# price = 12
# child_price = 8
# discount = 2 if day == "wednesday" else 0
# if age >= 18:
#     price -= discount
#     print(price, "a")
# else:
#     child_price -= discount
#     print(child_price, "b")

# 03 -------------------------------
# score = int(input("Enter your score :"))
# if score >= 101:
#     print("Please Enter Correct Number")
#     exit()

# if score >= 90:
#     print("Grade A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grafe C")
# else:
#     print("D")


# square_num = [x**2 for x in range(4)]
# print(square_num)


# question 4
# fruit = input("Enter Fruit Name :")
# color = input("Enter Fruite Color Name :").strip().lower()

# if color == "green":
#     print("Unripe")
# elif color == "yellow":
#     print("Ripe")
# elif color == "brown":
#     print("Overripe")

# question 5
# wheather = input("Enter Wheather :").strip().lower()
# listOfWheather = ["sunny", "rainy", "snowy"]
# if wheather in listOfWheather:
#     pass
# else:
#     print("Plesae Enter Correct Wheather")
#     exit()

# if wheather == "sunny":
#     activity = "Go for a walk"
# elif wheather == "rainy":
#     activity = "Read a book"
# elif wheather == "snowy":
#     activity = "Build a snowman"

# print(activity)
