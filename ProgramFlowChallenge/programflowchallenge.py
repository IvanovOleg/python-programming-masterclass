# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Example of the input you may get are:
#   127.0.01
#   .192.168.0.1
#   10.0.123456.255
#   172.16
#   255
#
# So your program should work even with invalid IP addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input test:
#   .123.45.678.91
#   123.4567.8.9.
#   123.156.289.10123456
#   10.10t.10.10
#   12.9.34.6.12.90
#   '' - tha is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

address = input("Please enter an IP address: ")
segments = []
segment = 0

for i in address:
    if i == '.':
        segments.append(segment)
        print("segment length is {}".format(segment))
        segment = 0
        continue
    else:
        segment += 1
else:
    segments.append(segment)
    print("segment length is {}".format(segment))

print("segment number is {}".format(len(segments)))
