# Modify the program from the Second Dictionary challenge of lecture 56
# to use shelves instead of dictionaries.
#
# Do this by creating two programs. cave_initialise.py should create the two
# shelves (locations and vocabulary) with the appropriate keys and values.
#
# cave_game.py will then use the two shelves instead of dictionaries.
# Apart from opening and closing the shelves, cave_game will need only
# two changes to the actual code - remember that shelf keys MUST be strings!
#
# Just to be clear, cave_game.py will contain the code from line 45, everything
# before that (modified to use shelves) will be in cave_initialise.py.

locations = {
    0: {
        "desc": "You are sitting in front of a computer learning Python",
        "exits": {},
        "namedExits": {}
    },
    1: {
        "desc": "You are standing at the end of a road before a small brick building",
        "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}
    },
    2: {
        "desc": "You are at the top of the hill",
        "exits": {"N": 5, "Q": 0},
        "namedExits": {"5": 5}
    },
    3: {
        "desc": "You are inside a building, a well house for a small stream",
        "exits": {"W": 1, "Q": 0},
        "namedExits": {"1": 1}
    },
    4: {
        "desc": "You are in a valley beside a stream",
        "exits": {"N": 1, "W": 2, "Q": 0},
        "namedExits": {"1": 1, "2": 2}
    },
    5: {
        "desc": "You are in the forest",
        "exits": {"W": 2, "S": 1, "Q": 0},
        "namedExits": {"2": 2, "1": 1}
    }
}

words = {
    "QUIT": "Q",
    "WEST": "W",
    "NORTH": "N",
    "EAST": "E",
    "SOUTH": "S",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5"
}

loc = 1

while True:

    availableExits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    if direction in allExits:
        loc = allExits[direction]
    elif direction in words.keys():
        loc = locations[loc]["exits"][words[direction]]
    else:
        print("You cannot go in that direction")