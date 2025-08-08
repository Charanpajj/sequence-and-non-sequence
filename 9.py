
a = 'Hyd'
print(a[0])      # Output: H
                 # Explanation: Accesses the character at index 0 (the first character) of the string 'a'.

print(a[1])      # Output: y
                 # Explanation: Accesses the character at index 1 (the second character) of the string 'a'.

print(a[2])      # Output: d
                 # Explanation: Accesses the character at index 2 (the third character) of the string 'a'.

#print(a[3])      # Output: IndexError: string index out of range
                 # Explanation: The string 'Hyd' only has indices 0, 1, and 2. Index 3 is out of bounds.

print(a[-1])     # Output: d
                 # Explanation: Accesses the character at the last position using negative indexing.

print(a[-2])     # Output: y
                 # Explanation: Accesses the character at the second to last position using negative indexing.

print(a[-3])     # Output: H
                 # Explanation: Accesses the character at the third to last position (which is the first character) using negative indexing.

#print(a[-4])     # Output: IndexError: string index out of range
                 # Explanation: The string 'Hyd' only has negative indices -1, -2, and -3. Index -4 is out of bounds.

print(a[0] == a[-3]) # Output: True
                     # Explanation: Both a[0] and a[-3] refer to the character 'H', so the comparison is true.

# a[2] = 'c'     # Output: TypeError: 'str' object does not support item assignment
                 # Explanation: Strings in Python are immutable, meaning you cannot change individual characters after the string is created.

# print(25[0])   # Output: TypeError: 'int' object is not subscriptable
                 # Explanation: Integers are not sequences and do not support indexing.

print('25'[0])   # Output: 2
                 # Explanation: '25' is a string, and [0] correctly accesses its first character.

# print(True[1]) # Output: TypeError: 'bool' object is not subscriptable
                 # Explanation: Boolean values are not sequences and do not support indexing.

print('True'[1]) # Output: r
                 # Explanation: 'True' is a string, and [1] correctly accesses its second character.

