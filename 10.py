a = 'Hyd'
print(a * 3)
# Output: HydHydHyd
# Explanation: The string 'a' is repeated 3 times.

print(a * 2)
# Output: HydHyd
# Explanation: The string 'a' is repeated 2 times.

#print(a * 1)
# Output: Hyd
# Explanation: The string 'a' is repeated 1 time.

print(a * 0)
# Output:
# Explanation: The string 'a' is repeated 0 times, resulting in an empty string.

print(a * -1)
# Output:
# Explanation: The string 'a' is repeated -1 times, which also results in an empty string. Python treats negative repetitions the same as zero repetitions for strings.

print(25 * 3)
# Output: 75
# Explanation: Standard multiplication of two integers.

print('25' * 3)
# Output: 252525
# Explanation: The string '25' is repeated 3 times.

#print('25' * 4.0)
# Output: TypeError: can't multiply sequence by non-int of type 'float'
# Explanation: String multiplication (repetition) only works with an integer. You cannot multiply a string by a float.

print(3 * 'Hyd')
# Output: HydHydHyd
# Explanation: The string 'Hyd' is repeated 3 times. The order of the string and integer in multiplication doesn't matter.

print('25' * True)
# Output: 25
# Explanation: In Python, True is treated as 1 in numerical contexts. So, '25' is repeated 1 time.

