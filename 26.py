a = [ ]
print(a)
# Output: []
# Explanation: This prints the empty list that has just been created and assigned to the variable 'a'.

a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
# Explanation: These statements add the specified elements to the end of the list 'a'.

print(a)
# Output: [25, 10.8, 'Hyd', True]
# Explanation: This prints the list after the four elements have been appended.

a . remove('Hyd')
# Explanation: This statement removes the first occurrence of the element with the value 'Hyd' from the list.

print(a)
# Output: [25, 10.8, True]
# Explanation: This prints the list after 'Hyd' has been successfully removed.

#a . remove('25')
# Output: Value Error: list.remove(x): x not in list
# Explanation: This statement attempts to remove the string '25' from the list. However, the list contains the integer `25`, not the string `'25'`. Since the `remove()` method requires an exact match of the value and type, and the value `'25'` is not present, a `Value Error` is raised. The program stops at this point.

print(a)
# Output: (This line would not be reached due to the Value Error above)
