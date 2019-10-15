import shelve

books = shelve.open("Fileio/books")
books["receipes"] = {
    "blt": ["bacon", "letucce", "tomato", "bread"],
    "beans_on_toast": ["beans", "bread"],
    "scrambled eggs": ["eggs", "butter", "milk"],
    "soup": ["tin of soup"],
    "pasta": ["pasta", "cheese"]
}

books["maintenance"] = {
    "stuck": ["oil"],
    "loose": ["gaffer tape"]
}

print(books["receipes"]["soup"])
print(books["receipes"]["scrambled eggs"])

print(books["maintenance"]["loose"])

books.close()
