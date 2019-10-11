# t = "a", "b", "C"

# # t = ("a", "b", "c")
# print(t)

# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Comany", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More MAyem", "Emilda May", 2011
metallica = "Ride the Lighting", "Metallica", 1984

print(metallica)
print(metallica[0])

# metallica[0] = "test" # will not work because tuple is imutable

imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

metallica2 = ["Ride the lighting", "Metallica", 1984]
print(metallica2)
metallica2[0] = ""
print(metallica2)

title, artist, year = metallica2
print(artist)