a = 'A'

# print(a[1])
# Output: Index Error: string index out of range
# Explanation: The string 'A' has only one character at index 0. There is no character at index 1. Accessing an index that does not exist results in an IndexError.

# print(a[1:])
# Output: (empty string)
# Explanation: This is a string slice operation. It attempts to slice from index 1 to the end of the string. Since index 1 is beyond the end of the string (which only has index 0), the slice returns an empty string.
