print(complex(3 , 4))
# Output: (3+4j)
# Explanation: Creates a complex number where the real part is 3 and the imaginary part is 4.

print(complex(0 , 4))
# Output: 4j
# Explanation: Creates a complex number where the real part is 0 and the imaginary part is 4. Python omits the '0+' when the real part is zero.

print(complex(3))
# Output: (3+0j)
# Explanation: Creates a complex number where the real part is 3 and the imaginary part defaults to 0.

print(complex(3.8 , 4.6))
# Output: (3.8+4.6j)
# Explanation: Creates a complex number where the real part is 3.8 and the imaginary part is 4.6 (both floats are retained).

print(complex(3.8))
# Output: (3.8+0j)
# Explanation: Creates a complex number where the real part is 3.8 and the imaginary part defaults to 0.

print(complex(3 , 4.5))
# Output: (3+4.5j)
# Explanation: Creates a complex number where the real part is 3 and the imaginary part is 4.5.

print(complex(True , False))
# Output: (1+0j)
# Explanation: Booleans are treated as their integer equivalents (True=1, False=0). So, it's complex(1, 0).

print(complex(True))
# Output: (1+0j)
# Explanation: True is treated as 1, and the imaginary part defaults to 0.

print(complex(False))
# Output: 0j
# Explanation: False is treated as 0, and the imaginary part defaults to 0. Python omits '0+0j' as just '0j'.

print(complex(True , 4))
# Output: (1+4j)
# Explanation: True is treated as 1 for the real part, and 4 is used for the imaginary part.

print(complex('3'))
# Output: (3+0j)
# Explanation: Parses the string '3' as the real part. The imaginary part defaults to 0.

print(complex('3.8'))
# Output: (3.8+0j)
# Explanation: Parses the string '3.8' as the real part (a float). The imaginary part defaults to 0.
'''
print(complex(3 , '4'))
# Output: TypeError: complex() second argument must be a number, not a str
# Explanation: When two arguments are provided to `complex()`, both must be numbers (int, float, bool). A string cannot be directly used as the imaginary part in this form.

print(complex('3' , 4))
# Output: TypeError: complex() can't take second arg if first is a string
# Explanation: If the first argument to `complex()` is a string, it is expected to be the *entire* complex number in string form (e.g., "3+4j"). You cannot provide a separate second argument (imaginary part) if the first argument is a string.

print(complex('3' , '4'))
# Output: TypeError: complex() can't take second arg if first is a string
# Explanation: Similar to the previous case, if the first argument is a string, a second string argument is not allowed.

print(complex('Ten'))
# Output: ValueError: complex() arg is a malformed string
# Explanation: The string 'Ten' cannot be parsed as a valid complex number. It must be in a numeric format (e.g., "3", "3.14", "2+5j").

'''