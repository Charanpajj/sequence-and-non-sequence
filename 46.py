#a = { [ ] : 25}
# Output: Type Error: unhashable type: 'list'
# Explanation: Dictionary keys must be "hashable" (immutable). A list (`[]`) is a mutable object, so it cannot be used as a key. This error stops the program's execution.

# The following lines of code would produce the outputs below if run independently.

b = { ( ) : 25}
print(b)
# Output: {(): 25}
# Explanation: A tuple `()` is immutable and thus hashable, so it can be used as a dictionary key.

#c = { { } : 25}
# Output: Type Error: unhashable type: 'set'
# Explanation: A set `{}` is a mutable object and cannot be used as a dictionary key.

d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)
# Output: {'Ramesh': [9948250500, 9848565090, 9440250404]}
# Explanation: The key 'Ramesh' is an immutable string and is valid. The value (a list of numbers) can be a mutable object.

print(len(d))
# Output: 1
# Explanation: The dictionary has one key-value pair.

#e = {set() : 10.8}
# Output: Type Error: unhashable type: 'set'
# Explanation: A set is a mutable object and cannot be used as a dictionary key.
