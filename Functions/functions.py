def python_food():
    width = 80
    text = "Spam and eggs"
    left_marging = (width -len(text)) // 2
    print(" " * left_marging, text)


# def centre_text(text):
#     text = str(text)
#     left_marging = (80 -len(text)) // 2
#     print(" " * left_marging, text)


# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_marging = (80 -len(text)) // 2
#     #print(" " * left_marging, text, end=end, file=file, flush=flush)
#     return " " * left_marging, text

def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_marging = (80 -len(text)) // 2
    #print(" " * left_marging, text, end=end, file=file, flush=flush)
    return " " * left_marging + text

# with open("Functions/centered.txt", mode='w') as centered_file:

#     # python_food()
#     centre_text("spam and eggs", file=centered_file)
#     centre_text(12, file=centered_file)
#     # print(python_food()) # Each Python function returns something or None

#     # print("first", "second", 3, 4, "spam")
#     centre_text("first", "second", 3, 4, "spam", sep=":", file=centered_file)


s1 = centre_text("spam and eggs")
print(s1)
print(centre_text(12))
print(centre_text("first", "second", 3, 4, "spam", sep=":"))
