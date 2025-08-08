a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}

print(a)
# Output: {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
# Explanation: Prints the dictionary as a literal.

print(type(a))
# Output: <class 'dict'>
# Explanation: Shows that the data type of the variable `a` is a dictionary.

print(a[10])
# Output: Ramesh
print(a[20])
# Output: Kiran
print(a[15])
# Output: Amar
print(a[18])
# Output: Sita
# Explanation: Dictionary values are accessed by placing their key inside square brackets.

# Errors during program execution

#print(a[19])
# Output: Key Error: 19
# Explanation: This key does not exist in the dictionary. Attempting to access it raises a `Key Error`.

#print(a[0])
# Output: Key Error: 0
# Explanation: The key `0` does not exist in the dictionary.

#print(a['Amar'])
# Output: Key Error: 'Amar'
# Explanation: The value 'Amar' is not a key. Dictionary values cannot be accessed using their values.

# The following code demonstrates how to modify the dictionary:

# Modify the value of key 15
a[15] = 'Krishna'
# The dictionary is now: {10: 'Ramesh', 20: 'Kiran', 15: 'Krishna', 18: 'Sita'}

# Remove the key-value pair 20 : 'Kiran'
del a[20]
# The dictionary is now: {10: 'Ramesh', 15: 'Krishna', 18: 'Sita'}

# Add a new key-value pair 25 : 'Vamsi'
a[25] = 'Vamsi'
# The dictionary is now: {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}

print(a)
# Output: {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
# Explanation: Prints the dictionary after all modifications.

print(len(a))
# Output: 4
# Explanation: The dictionary started with 4 elements, one was removed and one was added, so the length remains 4.

#print(a * 2)
# Output: Type Error: unsupported operand type(s) for *: 'dict' and 'int'
# Explanation: Dictionaries do not support the multiplication operator. This results in a `Type Error`.


