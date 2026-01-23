# # dictinoary

# foodTypes = {
#     "Biryani": "Spicy",
#     "Pulao": "Beef",
#     "ColdDrink": "Cola Next",
# }
# # print(foodTypes)

# foodTypes["Biryani"] = "Hot"
# # print(foodTypes)

# foodTypes["Stater"] = "Stack"

# # for food in foodTypes:
# #     print(food)

# foodTypes.pop("ColdDrink")
# foodTypes.popitem()
# del foodTypes["Pulao"]

# for key, value in foodTypes.items():
#     print(
#         key,
#         value,
#     )


dictinoary = {
    "Bags": {
        "Handle": "Padded Grip",
        "Material": "Polyester",
        "Color": "Black",
        "Size": "15 inch",
    },
    "Shoes": {
        "Type": "Sneakers",
        "SizeRange": [6, 12],
        "ColorOptions": ["Black", "White", "Grey"],
        "Brand": "GenericBrand",
    },
}

# print(dictinoary)
dictinoary["Bags"]["Color"] = "White"
print(dictinoary["Bags"]["Color"])

square_num = {x**2 for x in range(5)}
print(square_num)
