import shelve

locations = {
    "0": {
        "desc": "You are sitting in front of a computer learning Python",
        "exits": {},
        "namedExits": {}
    },
    "1": {
        "desc": "You are standing at the end of a road before a small brick building",
        "exits": {"W": "2", "E": "3", "N": "5", "S": "4", "Q": "0"},
        "namedExits": {"2": "2", "3": "3", "5": "5", "4": "4"}
    },
    "2": {
        "desc": "You are at the top of the hill",
        "exits": {"N": "5", "Q": "0"},
        "namedExits": {"5": "5"}
    },
    "3": {
        "desc": "You are inside a building, a well house for a small stream",
        "exits": {"W": "1", "Q": "0"},
        "namedExits": {"1": "1"}
    },
    "4": {
        "desc": "You are in a valley beside a stream",
        "exits": {"N": "1", "W": "2", "Q": "0"},
        "namedExits": {"1": 1, "2": 2}
    },
    "5": {
        "desc": "You are in the forest",
        "exits": {"W": "2", "S": "1", "Q": "0"},
        "namedExits": {"2": "2", "1": "1"}
    }
}

vocabulary = {
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

with shelve.open("Fileio/locations") as locations_shelve:
    for location in locations:
        locations_shelve[str(location)] = locations[location]

    for location in locations_shelve:
        print(location)
    print("Shelve location[0] is {}".format(locations_shelve['0']))

with shelve.open("Fileio/vocabulary") as vocabulary_shelve:
    for word in vocabulary:
        vocabulary_shelve[word] = vocabulary[word]
    
    for word in vocabulary_shelve:
        print(word)
    
