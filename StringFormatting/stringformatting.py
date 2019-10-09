age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))
print(
    """ January: {2}
    February: {0}
    April: {1}""".format(28,30,31)
)

print("My age is %d years" % age) #old 

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))


for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3)) # left formatted

print("Pi is aproximately {0:12.50}".format(22 / 7))
