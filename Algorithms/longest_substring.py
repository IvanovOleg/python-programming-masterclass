# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def find_length(string):
    output = ""
    for i, j in enumerate(string):
        result = ""
        for _, v in enumerate(string[i::]): # pwwkew, wwkew, wkew, kew, ew, w
            if v not in result:
                result = result + v
            else:
                break
        # print(result) pw, w, wke, kew, ew, w
        if len(output) < len(result):
            output = result
    return len(output)

# print(find_length("pwwkew"))
print(find_length("abcabcbb"))
