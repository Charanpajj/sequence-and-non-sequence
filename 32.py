a = [25]
#print(a[1])
# Output: Index Error: list index out of range
# Explanation: The list 'a' has only one element at index 0. There is no element at index 1. Attempting to access an index that does not exist raises an `Index Error`.

print(a[1:])
# Output: []
# Explanation: This is a slice operation. It attempts to create a new list containing elements from index 1 to the end. Since index 1 is beyond the end of the list, the slice is empty. Slicing does not raise an error when indices are out of bounds; it simply returns an empty list.
print(a[0:])