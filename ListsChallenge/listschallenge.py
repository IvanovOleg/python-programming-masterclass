# Add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "becon", "spam"])
menu.append(["egg", "becon", "sausage","spam"])
menu.append(["spam", "becon", "sausage","spam"])
menu.append(["spam", "egg", "spam","spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage","spam"])

print(menu)

for meal in menu:
    if not "spam" in meal:
        for ingredient in meal:
            print(ingredient)
        print(meal)
