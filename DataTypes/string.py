# string Method in python


userName = "Ammar Amir"
stringList = "A , B , C , D"
user = "  helloworld         "
count = "A A B A C D A"
brand = "Nike"
shoes = "Shoes"
order = "i order {} ten {}"
myList = ["A", "b", "C", "D", "E"]
x = 'he said "football is a good game" '
print(userName.upper())
print(userName.lower())
print(userName.replace("Amir", "Tahir"))
print(userName.startswith("A"))
print(userName.find("m"))
print(stringList.split(","))
print(userName[0:5])
print(userName[:5])
print(userName[5:])
print(user.strip())
print(count.count("A"))
print(order.format(brand, shoes))
print(" - ".join(myList))
print(len(userName))
print(x)
print("He" in x)
