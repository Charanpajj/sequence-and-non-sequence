list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']

print(list[2 : 7])
# Output: [(3+4j), 'Hyd', True, None, 10.8]
# Explanation: Slices from index 2 (inclusive) up to, but not including, index 7.

print(list[ : : ])
# Output: [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
# Explanation: Slices the entire list from start to end with a step of 1, creating a shallow copy.

print(list[:])
# Output: [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
# Explanation: Same as the above. An empty slice returns a shallow copy of the entire list.

print(list[ : : -1])
# Output: ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
# Explanation: Slices the entire list with a step of -1, which reverses the order of the elements.

print(list[ : : 2])
# Output: [25, (3+4j), True, 10.8]
# Explanation: Slices from the beginning to the end, taking every second element (at indices 0, 2, 4, 6).

print(list[1 : : 2])
# Output: [10.8, 'Hyd', None, 'Hyd']
# Explanation: Slices from index 1 to the end, taking every second element (at indices 1, 3, 5, 7).

print(list[ : : -2])
# Output: ['Hyd', None, True, 10.8]
# Explanation: Slices from the end of the list to the beginning, taking every second element (at indices -1, -3, -5, -7). The provided note in the prompt contains a typo for the output.

print(list[-2 : : -2])
# Output: [10.8, True, (3+4j), 25]
# Explanation: Slices from index -2 to the beginning, taking every second element (at indices -2, -4, -6, -8).

print(list[1 : 4])
# Output: [10.8, (3+4j), 'Hyd']
# Explanation: Slices from index 1 (inclusive) up to, but not including, index 4.

print(list[-4 : -1])
# Output: [True, None, 10.8]
# Explanation: Slices from index -4 (inclusive) up to, but not including, index -1.

print(list[3 : -3])
# Output: ['Hyd', True]
# Explanation: Slices from index 3 (inclusive) up to, but not including, index -3. Index -3 corresponds to `None`. The slice includes elements at indices 3 and 4.

print(list[2 : -5])
# Output: [(3+4j)]
# Explanation: Slices from index 2 (inclusive) up to, but not including, index -5. Index -5 corresponds to `3 + 4j`. The slice only contains the single element at index 2.

print(list[-1:-5])
# Output: []
# Explanation: Slicing with a positive step (the default) requires the start index to be less than the stop index. Since -1 is greater than -5, this slice results in an empty list.
