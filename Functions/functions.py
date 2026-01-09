import math


def square_of_number(num):
    return num**2


# print(square_of_number(3))


def circle_stats(raduis):
    # formula of area
    area = math.pi * raduis**2
    # formula of circumference
    circumference = 2 * math.pi * raduis
    return area, circumference


a, c = circle_stats(5)
# print("Area :", a, "Circumference :", c)


def add(num1, num2):
    return num1 + num2


print(add(2, 3))


def multiply(p1, p2):
    return p1 * p2


print(multiply("z", 3)) 


def greek_user(name="user"):
    return "Hello" + " " + name + "!"


print(greek_user("fajar"))


