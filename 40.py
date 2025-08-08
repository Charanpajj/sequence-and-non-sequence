a = [ ]
b = ( )
c = {}
d = set()

print(type(a))
# Output: <class 'list'>
# Explanation: The `[]` literal syntax creates an empty list.

print(type(b))
# Output: <class 'tuple'>
# Explanation: The `()` literal syntax creates an empty tuple.

print(type(c))
# Output: <class 'dict'>
# Explanation: This is a common point of confusion. The `{}` literal syntax creates an empty **dictionary**, not a set.

print(type(d))
# Output: <class 'set'>
# Explanation: The `set()` constructor must be used to create an empty set.

print(a)
# Output: []
# Explanation: Prints the empty list.

print(b)
# Output: ()
# Explanation: Prints the empty tuple.

print(c)
# Output: {}
# Explanation: Prints the empty dictionary.

print(d)
# Output: set()
# Explanation: Prints the empty set. Python's representation of an empty set is `set()` to distinguish it from the empty dictionary literal `{}`.

