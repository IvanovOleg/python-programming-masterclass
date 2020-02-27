# Given a non-empty array N, of non-negative integers. The degree of this array is defined as
# the maximum frequency of any one of it's elements. Your task is to find the smallest possible
# length of a (contiguous) subarray of N, that has the same degree as N. For example, in the array
# [1 2 2 3 1], integer 2 occurs maximum of twice. Hence the degree is 2.

# Input

# Test case input contains 2 lines. First line contains an integer T, representing the number of
# elements in the array. The second line contains the array N, list of T integers each separated
# by space.

# Output

# Print the length of the smallest contiguous subarray of input array N, that has the same degree as N.
# Code evaluation is based on your output, please follow the sample format and do NOT print anything else.

# Sample Input

# 5
# 1 2 2 3 1

# Sample Output

# 2

def size(array):
    left, right, count = {}, {}, {}

    for k, v in enumerate(array):
        if v not in left.keys(): left[v] = k
        right[v] = k
        count[v] = count.get(v, 0) + 1
    
    degree = max(count.values())
    size = len(array)

    for i in count:
        if count[i] == degree:
            size = right[i] - left[i] + 1

    return size

def get_array(string):
    return list(map(lambda x: int(x), string.split('\n')[1].split(' ')))

print(size(get_array('5\n1 2 2 3 1')))
