# list in python


cars = ["corolla", "alto", "civic", "haval", "kia"]
# print(cars)
# print(cars[1])
# print(cars[2:6])
# print(cars[:2])
# print(cars[2:])
# cars[0] = "BMW"
# print(cars)
# cars[1:4] = ["Lambo", "Buggati", "G-Wagon"]
# print(cars)
# print(cars[1:1])
# cars[1:1] = ["P", "P"]
# print(cars)
# cars[1:3] = []
# print(cars)


# cars.append("Porsche")
cars.extend(["Porsche", "pagani"])
cars.remove("corolla")
cars.pop(0)
cars.insert(1, "Move")
print(cars)
