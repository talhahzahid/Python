import time
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, -9, 10]
# positive_number_count = 0

# for num in numbers:
#     if num > 0:
#         positive_number_count += 1

# print(positive_number_count)

# question 2
n = 10
sum_even = 0

# for i in range(10):
#     if i % 2 == 0:
#         sum_even += 1

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum_even += 1

# print(sum_even)


# question 3

# number = 5

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, "X", i, "=", number * i)

# question 4
# string = "Talha"
# reversed_str = ""
# for i in string:
#     reversed_str = i + reversed_str

# print(reversed_str)

# question 5
# value = "ttteaaeeagcls"
# for char in value:
#     # print(char)
#     if value.count(char) == 1:
#         print(char)
#         break

# question 6

number = 7
factorial = 1


while number > 0:
    # print(number)
    factorial = number * factorial
    number = number - 1

# print(factorial, "factorial")

# factorial ///  7 42 210 840 2520 5040
# number    ///  6 5  4   3   2    1

# question 7

# while True:
#     number = int(input("Enter number b/w 1 to 10: "))
#     if number >= 1 and number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Try again")

# question 8

number = 71

is_prime = True

for i in range(1, number):
    if number % i == 0:
        is_prime = False
        break

# print(is_prime)


wait_time = 1
max_retries = 5
attemps = 0

while attemps < max_retries:
    print("attemps", attemps + 1, "wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attemps += 1
