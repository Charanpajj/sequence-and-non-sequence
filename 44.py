a = {10 : 'Hyd' , 10 : 'Sec'}
# Explanation: Dictionaries cannot have duplicate keys. When a key is repeated during creation, the last value associated with that key overwrites any previous values.

print(a)
# Output: {10: 'Sec'}
# Explanation: The second entry for key 10 (`'Sec'`) overwrites the first (`'Hyd'`). The final dictionary contains only one key-value pair.

print(len(a))
# Output: 1
# Explanation: The length of the dictionary is the number of unique keys, which is 1.

b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
# Explanation: Similar to the above, the values for the duplicate keys 'G' and 'B' are overwritten by their last-assigned values.

print(b)
# Output: {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
# Explanation: The final dictionary contains only the unique keys with their last assigned values. The order of keys is typically preserved in modern Python versions (3.7+).

print(len(b))
# Output: 4
# Explanation: The dictionary has 4 unique keys: 'R', 'G', 'B', and 'Y'.

