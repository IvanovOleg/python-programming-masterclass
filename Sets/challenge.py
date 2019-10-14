# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

text_string = "My name is Oleg."
vowels = frozenset("aeiouyAEIOUY")

text_set = set(text_string)

print(sorted(list(text_set.difference(vowels))))
