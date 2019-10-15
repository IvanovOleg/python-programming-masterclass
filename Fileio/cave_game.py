import shelve

loc = "1"

locations = shelve.open("Fileio/locations")
vocabulary = shelve.open("Fileio/vocabulary")

for location in locations:
    print(location)
print(locations[loc]['exits'].keys())

while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    if direction in allExits:
        loc = allExits[direction]
        print("loc is: {}".format(loc))
    elif direction in vocabulary.keys():
        loc = locations[loc]["exits"][vocabulary[direction]]
    else:
        print("You cannot go in that direction")

locations.close()
vocabulary.close()
