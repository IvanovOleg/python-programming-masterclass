# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# parrot_list = ["no pinnin'", "no more", "a stiff", "bereft of live"]
# parrot_list.append("A Norwegian Blue")

# for state in parrot_list:
#     print("This parrot is " + state)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7]

# numbers = even + odd
# #numbers.sort()

# ordered_numbers = sorted(numbers)
# print(ordered_numbers)

# if numbers == ordered_numbers:
#     print("Lists are equal")
# else:
#     print("Lists are not equal")

# if ordered_numbers == sorted(numbers):
#     print("Lists are equal")
# else:
#     print("Lists are not equal")

# list_1 = []
# list_2 = list()

# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))

# if list_1 == list_2:
#     print("Lists are equal")
# else:
#     print("Lists are not equal")

# print(list(("Lists are not equal"))

# even = [2, 4, 6, 8]
# # another_even = even # same list
# another_even = list(even) # new list

# another_even = sorted(even, reverse=True) # new list

# print(another_even == even)
# print(another_even is even)

# another_even.sort(reverse=True)
# print(even) # [8, 6, 4, 2]
# print(another_even) # [8, 6, 4, 2]

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7]

# numbers = [even, odd]
# print(numbers)

# for number_set in numbers:
#     print(number_set)
#     for value in number_set:
#         print(value)

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
        print(meal)
