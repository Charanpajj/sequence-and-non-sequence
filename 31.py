a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))
# Output: [10, 20, 30, 40, 50] [A unique memory address, e.g., 2049082728944]
# Explanation: This prints the initial list and its memory address.

a[1 : 4] = [60 , 70]
print(a , id(a))
# Output: [10, 60, 70, 50] [The same memory address as before]
# Explanation: This is a slice assignment. The elements at indices 1, 2, and 3 ([20, 30, 40]) are replaced by the new list [60, 70]. The list is modified *in place*, so the memory address remains the same.

a[2: 4] = [100 , 200 , 300]
print(a , id(a))
# Output: [10, 60, 100, 200, 300] [The same memory address as before]
# Explanation: The list `a` is now `[10, 60, 70, 50]`. This statement replaces the elements at indices 2 and 3 ([70, 50]) with the new list [100, 200, 300]. The list is modified in place again, so the memory address does not change.

