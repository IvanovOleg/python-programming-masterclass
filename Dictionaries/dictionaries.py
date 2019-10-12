fruit = {
    "orange": "a sweet, orange, citrus fuit",
    "apple": "god for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fuit growing in bunches",
    "lime": " a sour, green citrus fruit"
}

# print(fruit)
# print(fruit["lemon"])

# fruit["pear"] = "an odd shaped apple"
# print(fruit)

# fruit["lime"] = "great with tequila"
# print(fruit)

#del fruit["lemon"]
#del fruit
# fruit.clear()
# print(fruit)
# print(fruit["tomato"]) # error because that key doesn't exist

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key) # doesn't return an error if doesn't exist, returns None instead
#         print(description)
#     else:
#         print("we dont have a " + dict_key)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key) # doesn't return an error if doesn't exist, returns None instead
#     print(description)

# for snack in fruit:
#     print(fruit[snack])

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)

# for key in fruit.keys():
#     print(fruit[key]) # more efficient than values

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

# print(fruit)
# print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
