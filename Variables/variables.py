# greeting = "Hello"
# _myName = "Oleg"
# Oleg45 = "Good"
# Oleg_Was_32 = "Hello"
# Greeting = "There"
# print(Oleg45 + ' ' + greeting)

# age = 32
# print(age)

# print(greeting + age)


#################################

# number
a = 12

b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b) # returns float 4.0
print(a // b) # returns integer 4
print(a % b) # returns reminder

for i in range(1, a//b):
    print(i)

print(a + b / 3 -4 * 12) # * and / has higher priority
print((((a + b) / 3) -4) * 12) # use brackets to force the order

c = a + b
d = c / 3
e = d -4
print(e * 12)


parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2]) # start, end, step

number = "9,223,372,036,854,775,807"
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) # 123456789 is usefull to extract a formatted data

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's " "probably " "pinning")

print("hello " * 5)

today = "friday"
print("day" in today)