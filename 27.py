a = [25 , 10.8 , 'Hyd']
print(a)
# Output: [25, 10.8, 'Hyd']
# Explanation: Prints the list `a` as it is defined.

print(id(a))
# Output: [A unique memory address, e.g., 2049082728944]
# Explanation: This prints the unique memory address of the list object `a`.

print(a * 3)
# Output: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
# Explanation: Creates and prints a new list containing the elements of `a` repeated 3 times.

print(a * 2)
# Output: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
# Explanation: Creates and prints a new list with the elements of `a` repeated 2 times.

print(a * 1)
# Output: [25, 10.8, 'Hyd']
# Explanation: Creates and prints a new list with the elements of `a` repeated 1 time, which is a shallow copy of the original list.

print(a * 0)
# Output: []
# Explanation: Creates and prints a new empty list.

print(a * -1)
# Output: []
# Explanation: Multiplies by a negative integer, which also results in a new empty list.

#print(a * 4.0)
# Output: TypeError: can't multiply sequence by non-int of type 'float'
# Explanation: List repetition (multiplication) only works with integers, not floats.

a = a * 3
# Explanation: The expression `a * 3` creates a *new* list object with repeated elements. The variable `a` is then reassigned to refer to this new list.

print(a)
# Output: [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
# Explanation: Prints the newly created, longer list that `a` now references.

print(id(a))
# Output: [A new and different memory address, e.g., 2049082729900]
# Explanation: This prints the memory address of the new list object. This address will be different from the original one, proving that a new object was created and the variable was reassigned.

a = [25]
# Explanation: `a` is reassigned to a new list containing just the integer 25.

#print(a * a)
# Output: Type Error: can't multiply sequence by non-int of type 'list'
# Explanation: Lists cannot be multiplied by other lists. The multiplication operator is only defined for multiplying a list by an integer.

