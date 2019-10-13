fruit = {
    "orange": "a sweet, orange, citrus fuit",
    "apple": "god for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fuit growing in bunches",
    "lime": " a sour, green citrus fruit"
}

print(fruit)

veg = {
    "cabbage": "every child's favorite",
    "sprouts": "mmmm, lovely",
    "spinach": "can I have some more fruit, please"
}

print(veg)

veg.update(fruit)

print(veg)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
