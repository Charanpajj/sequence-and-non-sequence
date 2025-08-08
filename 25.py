a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)
# Output: [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
# Explanation: This prints the entire list object, including the square brackets and the comma-separated elements. The complex number is printed with parentheses around it.

print(*a)
# Output: 25 10.8 Hyd True (3+4j) None Hyd 25
# Explanation: The `*` operator unpacks the list's elements, and the `print()` function then prints them as individual arguments, separated by spaces.

print(type(a))
# Output: <class 'list'>
# Explanation: This shows that the data type of the variable 'a' is a list.

print(id(a))
# Output: [A unique memory address, e.g., 2049082728944]
# Explanation: This prints the unique memory address in which the list object `a` is stored. The exact value will vary with each run.

print(len(a))
# Output: 8
# Explanation: The `len()` function returns the number of elements in the list, which is 8.

a[2] = 'Sec'
# Explanation: Lists are mutable. This statement replaces the element at index 2 (which was 'Hyd') with the new string 'Sec'.

print(a)
# Output: [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
# Explanation: This prints the modified list. The element at index 2 has been changed from 'Hyd' to 'Sec'. The memory address of the list itself remains the same because the list was modified in place.

print(a[2 : 5])
# Output: ['Sec', True, (3+4j)]
# Explanation: This is a slice operation. It creates a new list containing the elements from index 2 (inclusive) up to, but not including, index 5. The new list contains the modified element 'Sec', followed by the original elements True and (3+4j).
