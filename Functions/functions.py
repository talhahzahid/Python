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


# a, c = circle_stats(5)
# print("Area :", a, "Circumference :", c)


def add(num1, num2):
    return num1 + num2


# print(add(2, 3))


def multiply(p1, p2):
    return p1 * p2


# print(multiply("z", 3))


def greek_user(name="user"):
    return "Hello" + " " + name + "!"


# print(greek_user("fajar"))


# lambda fuctions


def cube(num):
    return num**3


# print(cube(5))


# cube = lambda x: x**3
# print(cube(3))


#  *args

# sum keyword  to sum all  number


# def sum_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total


# print(sum_all(2, 3, 2))

# print_kwargs(name="Ali")

