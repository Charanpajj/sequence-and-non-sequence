a = range(10 , 50 , 5)

print(type(a))
# Output: <class 'range'>
# Explanation: This prints the data type of the variable 'a', which is a 'range' object.

print(a)
# Output: range(10, 50, 5)
# Explanation: Printing a 'range' object directly shows its internal representation (start, end, step), rather than all the numbers it contains.

print(*a)
# Output: 10 15 20 25 30 35 40 45
# Explanation: The `*` operator unpacks the elements of the 'range' object and passes them as separate arguments to the `print()` function, which then prints them separated by spaces.

print(id(a))
# Output: [A unique memory address, e.g., 140700346337456]
# Explanation: This prints the unique memory address where the `range` object 'a' is stored. The actual address will be different each time the program runs.

print(len(a))
# Output: 8
# Explanation: The `len()` function calculates the number of elements in the range. The formula is (stop - start) // step, which is (50 - 10) // 5 = 40 // 5 = 8.

print(*a[2 : 7] , sep = ' , ')
# Output: 20 , 25 , 30 , 35 , 40
# Explanation: This first creates a slice of the 'range' object from index 2 (inclusive) to 7 (exclusive). This new range contains the numbers 20, 25, 30, 35, 40. The `*` operator unpacks these numbers and the `sep` argument specifies a comma and a space as the separator.

print(*a[ : : -1])
# Output: 45 40 35 30 25 20 15 10
# Explanation: This creates a reverse slice of the entire 'range' object (step is -1), which generates the numbers in reverse order. The `*` operator unpacks and prints them.
'''
# a[4] = 32
# Output: Type Error: 'range' object does not support item assignment
# Explanation: `range` objects are **immutable**, meaning their elements cannot be changed or modified after creation. Attempting to assign a new value to an index results in a `Type Error`.

# print(a * 2)
# Output: Type Error: unsupported operand type(s) for *: 'range' and 'int'
# Explanation: The `range` object does not support the multiplication operator. You cannot repeat or multiply a `range` object.
'''