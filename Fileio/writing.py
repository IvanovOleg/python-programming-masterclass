# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\cities.txt", 'w') as city_file:
#     for city in cities:
#         # print(city, file=city_file, flush=True)
#         print(city, file=city_file)

# cities = []

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n')) # added strip to remove \n from string
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# )

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\imelda.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\imelda.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents) # eval runs string as code, not the best idea
print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
