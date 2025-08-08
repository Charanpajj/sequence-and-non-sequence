a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}

print(a)
# Output: {True, None, 10.8, 25, 'Hyd', (3+4j)}
# Explanation: Sets are unordered collections of unique elements. The duplicate values (the second `25` and `Hyd`) are discarded. The order of elements in the output is not guaranteed and can vary between Python versions or runs. Note that `True` is not treated as `1` here, so both are included.

print(type(a))
# Output: <class 'set'>
# Explanation: This confirms the data type of the variable `a` is a set.

print(len(a))
# Output: 6
# Explanation: The `len()` function returns the number of unique elements in the set, which is 6.
'''
print(a[2])
# Output: Type Error: 'set' object is not subscriptable
# Explanation: Sets are unordered and do not support indexing or direct element access. A `Type Error` is raised.

print(a[1 : 4])
# Output: Type Error: 'set' object is not subscriptable
# Explanation: Similar to indexing, sets do not support slicing. A `TypeError` is raised.

a[2] = 'Sec'
# Output: Type Error: 'set' object does not support item assignment
# Explanation: Sets are mutable, but they do not support item assignment by index because they are unordered. You must use methods like `add()` or `remove()`.

print(a * 2)
# Output: Type Error: unsupported operand type(s) for *: 'set' and 'int'
# Explanation: The multiplication (repetition) operator is not supported for set objects.

print(a * a)
# Output: Type Error: unsupported operand type(s) for *: 'set' and 'set'
# Explanation: Sets cannot be multiplied by other sets.

'''