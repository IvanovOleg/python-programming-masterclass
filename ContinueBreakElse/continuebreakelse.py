# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item == 'spam':
#         continue # skips this iteration
#     print("Buy " + item)

# for item in shopping_list:
#     if item == 'spam':
#         break # exit from the loop
#     print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plat of that, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it")
