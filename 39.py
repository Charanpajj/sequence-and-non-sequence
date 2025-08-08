a = set('Rama rAo')
print(a)
# Output: {'R', 'a', 'm', ' ', 'r', 'o'}  (The order may vary)
# Explanation: The `set()` function takes the string and converts it into a set of its unique characters. Case matters ('R' and 'r' are different), and spaces are included.

print(len(a))
# Output: 6
# Explanation: There are 6 unique characters in the string "Rama rAo".

print(set([10 , 20 , 15 , 20]))
# Output: {10, 20, 15}  (The order may vary)
# Explanation: The `set()` function converts the list into a set, automatically removing the duplicate `20`.

print(set((25 , 10.8 , 'Hyd' , 10.8)))
# Output: {10.8, 'Hyd', 25}  (The order may vary)
# Explanation: The `set()` function converts the tuple into a set, automatically removing the duplicate `10.8`.

print(set(range(10 , 20 , 3)))
# Output: {10, 13, 16, 19}  (The order may vary)
# Explanation: The `range()` object is an iterable. The `set()` function converts it into a set of the numbers it generates.

#print(set(25))
# Output: Type Error: 'int' object is not iterable
# Explanation: The `set()` function requires an iterable object (like a string, list, or tuple) as its argument. An integer is not iterable, so a `Type Error` is raised.

#print(set([25 , 10.8 , [] , 'Hyd']))
# Output: Type Error: unhashable type: 'list'
# Explanation: Set elements must be "hashable" (immutable). A list (`[]`) is a mutable object and is therefore not hashable. This causes a `Type Error` when the `set()` function tries to add it as an element.

