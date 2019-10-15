# abber = open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\sample.txt", 'r')
# jabber = open("sample.txt", 'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')

# jabber.close()

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\sample.txt", 'r') as jabber: # with closes a file automatically
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\sample.txt", 'r') as jabber: # with closes a file automatically
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\sample.txt", 'r') as jabber: # with closes a file automatically
#     lines = jabber.readlines()
# print(lines)

# for line in lines:
#     print(line, end='')

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\sample.txt", 'r') as jabber: # with closes a file automatically
#     lines = jabber.readlines()
# print(lines)

# for line in lines[::-1]:
#     print(line, end='')

with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\sample.txt", 'r') as jabber: # with closes a file automatically
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')
