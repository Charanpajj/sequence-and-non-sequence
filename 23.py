a = range(10 , 20)
print(*a , sep = ',')
# Output: 10,11,12,13,14,15,16,17,18,19
# Explanation: A 'range' object is created with a starting value of 10 (inclusive) and an ending value of 20 (exclusive). The default step is 1. The `*` operator unpacks these numbers and the `sep` argument specifies a comma as the separator.

b = range(5)
print(*b)
# Output: 0 1 2 3 4
# Explanation: When `range()` is called with a single argument, it is treated as the stop value, with the start defaulting to 0 and the step defaulting to 1. The `*` operator unpacks and prints the numbers with a default space separator.

c = range(10 , 1 , -1)
print(*c , sep = '...')
# Output: 10...9...8...7...6...5...4...3...2
# Explanation: A 'range' is created starting at 10 and counting down to 1 (exclusive) with a step of -1. The `*` operator unpacks the numbers and the `sep` argument specifies '...' as the separator.

d = range(-10 , 0)
print(*d)
# Output: -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# Explanation: A 'range' is created starting at -10 (inclusive) and ending at 0 (exclusive) with a default step of 1.

e = range(-10)
print(*e)
# Output: (empty line)
# Explanation: When `range()` is called with a single negative argument, it is interpreted as `range(0, -10)`. Since the start (0) is greater than the stop (-10) and the step is positive (the default 1), the range is empty. Unpacking an empty sequence results in no output.

f = range(2 , 2)
print(*f)
# Output: (empty line)
# Explanation: The start and stop values are the same. Since the `range` function's stop value is exclusive, the range is empty. Unpacking an empty sequence results in no output.

#g = range(10 , 11 , 0.1)
#Output: Type Error: 'float' object cannot be interpreted as an integer
# Explanation: The `range()` function requires all its arguments (start, stop, and step) to be integers. A `Type Error` is raised when a float (0.1) is used as the step.

#h = range('A' , 'F')
# Output: Type Error: 'str' object cannot be interpreted as an integer
# Explanation: The `range()` function requires all its arguments to be integers. A `Type Error` is raised when strings are used.
