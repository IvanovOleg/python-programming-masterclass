# Output the first positive digit from the list

source_list = [-9, -7, -5, -4, -3, -2, -1, 0, 1, 2, 4, 5, 6, 7 ]
source_list_set = set(sorted(source_list))
positive_range_set = set(range(1, max(source_list)))

print(positive_range_set.difference(source_list_set))
