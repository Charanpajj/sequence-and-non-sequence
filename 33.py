a = (25)
b = 25,
c = 25
d = (25,)

print(type(a))
# Output: <class 'int'>
# Explanation: The parentheses around '25' are used for grouping and do not create a tuple. 'a' is simply assigned the integer 25.

print(type(b))
# Output: <class 'tuple'>
# Explanation: The comma after the number is the key to creating a tuple with a single element.

print(type(c))
# Output: <class 'int'>
# Explanation: This is a standard integer assignment. 'c' is assigned the integer 25.

print(type(d))
# Output: <class 'tuple'>
# Explanation: This is the standard, unambiguous syntax for creating a tuple with a single element. The parentheses and the comma together define the tuple.

print(a * 4)
# Output: 100
# Explanation: 'a' is an integer, so this performs standard integer multiplication (25 * 4).

print(b * 4)
# Output: (25, 25, 25, 25)
# Explanation: 'b' is a tuple. The multiplication operator on a tuple performs repetition, creating a new tuple with the elements of 'b' repeated 4 times.

print(c * 4)
# Output: 100
# Explanation: 'c' is an integer, so this performs standard integer multiplication (25 * 4).

print(d * 4)
# Output: (25, 25, 25, 25)
# Explanation: 'd' is a tuple. The multiplication operator on a tuple performs repetition, creating a new tuple with the elements of 'd' repeated 4 times.

