a = list('Hyd')
print(a)
# Output: ['H', 'y', 'd']
# Explanation: The `list()` function takes the string 'Hyd' (which is a sequence of characters) and creates a new list with each character as an element.

print(type(a))
# Output: <class 'list'>
# Explanation: This confirms that the data type of the variable 'a' is a list.

print(len(a))
# Output: 3
# Explanation: The `len()` function returns the number of elements in the list 'a', which is 3.

b = (10 , 20 , 15 , 18)
print(list(b))
# Output: [10, 20, 15, 18]
# Explanation: The `list()` function takes the tuple `b` (a sequence) and converts it into a new list.

print(list(range(5)))
# Output: [0, 1, 2, 3, 4]
# Explanation: The `range(5)` function creates a sequence of numbers from 0 to 4. The `list()` function converts this sequence into a list.

#print(list(25))
# Output: Type Error: 'int' object is not iterable
# Explanation: The `list()` function can only convert objects that are "iterable" (i.e., sequences like strings, tuples, lists, or ranges). An integer like 25 is not a sequence, so this conversion is not possible and a `Type Error` is raised.

