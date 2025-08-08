a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
# Explanation: These lines add elements to the set. Sets only store unique, hashable elements.
# - 'Hyd' is added once. The second `add('Hyd')` does nothing.
# - The integer `1` is considered equal to the boolean `True`. Since `True` was added first, the `a.add(1)` operation does not change the set's contents.
# The set `a` now contains 5 unique elements: `{True, None, 10.8, 25, 'Hyd'}` (order may vary).

print(a)
# Output: {True, None, 10.8, 25, 'Hyd'} (Order may vary)
# Explanation: Prints the final set after all additions.

print(len(a))
# Output: 5
# Explanation: The set contains 5 unique elements.

a . remove(25)
# Explanation: This removes the element 25 from the set.

print(a)
# Output: {True, None, 10.8, 'Hyd'} (Order may vary)
# Explanation: Prints the set after 25 has been removed. It now contains 4 elements.

#a . append(100)
# Output: Attribute Error: 'set' object has no attribute 'append'
# Explanation: Sets do not have an `append()` method. You must use `add()` to add a single element. This error stops the program's execution. The remaining lines in the code will not be executed.
