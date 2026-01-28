# # import time
# # numbers = [1, -2, 3, -4, 5, 6, -7, -8, -9, 10]
# # positive_number_count = 0

# # for num in numbers:
# #     if num > 0:
# #         positive_number_count += 1

# # print(positive_number_count)

# # question 2
# n = 10
# sum_even = 0

# # for i in range(10):
# #     if i % 2 == 0:
# #         sum_even += 1

# # for i in range(1, n + 1):
# #     if i % 2 == 0:
# #         sum_even += 1

# # print(sum_even)


# # question 3

# # number = 5

# # for i in range(1, 11):
# #     if i == 5:
# #         continue
# #     print(number, "X", i, "=", number * i)

# # question 4
# # string = "Talha"
# # reversed_str = ""
# # for i in string:
# #     reversed_str = i + reversed_str

# # print(reversed_str)

# # question 5
# # value = "ttteaaeeagcls"
# # for char in value:
# #     # print(char)
# #     if value.count(char) == 1:
# #         print(char)
# #         break

# # question 6

# number = 7
# factorial = 1


# while number > 0:
#     # print(number)
#     factorial = number * factorial
#     number = number - 1

# print(factorial, "factorial")

# # factorial ///  7 42 210 840 2520 5040
# # number    ///  6 5  4   3   2    1

# # question 7

# # while True:
# #     number = int(input("Enter number b/w 1 to 10: "))
# #     if number >= 1 and number <= 10:
# #         print("Thanks")
# #         break
# #     else:
# #         print("Try again")

# # question 8

# number = 71

# is_prime = True

# for i in range(1, number):
#     if number % i == 0:
#         is_prime = False
#         break

# # print(is_prime)


# # wait_time = 1
# # max_retries = 5
# # attempts = 0

# # while attempts < max_retries:
# #     print("attempts", attempts + 1, "wait time", wait_time)
# #     time.sleep(wait_time)
# #     wait_time *= 2
# #     attempts += 1


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_num = 0

# for i in list:
#     if i % 2 != 0:
#         even_num += 1


# # print(even_num)

# password = ""

# while password != "1234":
#     password = input("enter password: ")
#     if password != "1234":
#         print("incorrect password")

# print("access")


#  even number

# numbers = [
#     1,
#     2,
#     3,
#     45,
#     3,
#     -3,
#     5,
#     6,
# ]
# is_prime = 0
# for i in numbers:
#     if i % 2:
#         is_prime += 1

# print(is_prime)

# -------------


# question 2
# for i in range(1, 21):
#     print(i)

# question 3
# number = int(input("Enter Table Number "))
# for i in range(1, 11):
#     print(number, "*", i, "=", i * number)

# question 4
# number = int(input("Enter Number "))

# for i in range(2, number):
#         if number % i == 0:
#             print("Not a prime")
#             # break
#         else:
#             print("Prime")

# # if number % 2 == 0:
# #     print("even")
# # else:
# #     print("odd")

# question 5
# total = 0
# for i in range(1, 101):
#     total += i

# print(total)

# question 6
# number = 7
# factorial = 1

# while number > 0:
#     factorial = number * factorial
#     number = number - 1

# print(factorial)

# # # question 7
# number = int(input("Enter Number we are calculate the length of number "))
# for i in number.split(","):
#     print(i)
#     # print(len(i))

# str = "*"
# for i in str:
#     print(i)

# number = 5

# while number > 0:
#     print("*" * number)
#     number -= 1

# number = input("Enter a number: ")
# print("Reversed:", number[::-1])

# question 1
# number = int(input("Enter Number "))
# total = 0
# for i in range(1, number + 1):
#     if i % 2 == 0:
#         total = total + 1

# print("total prime number is", total)


# question 2
text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowels:", count)
