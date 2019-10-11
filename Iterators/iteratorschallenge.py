# Create a list of items (you may use eiter string or number in the list)
# then create an iterator using iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# Hint: use the len() function rather than counting the number of items in the list.

list_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(len(list_items))
list_iterator = iter(list_items)

for i in range(len(list_items)):
    print(next(list_iterator))
