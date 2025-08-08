print(float(25))
# Output: 25.0
# Explanation: Converts the integer 25 to a float 25.0.

print(float(True))
# Output: 1.0
# Explanation: Converts the boolean True to its float equivalent, which is 1.0.

print(float(False))
# Output: 0.0
# Explanation: Converts the boolean False to its float equivalent, which is 0.0.

print(float('92'))
# Output: 92.0
# Explanation: Converts the string '92' (representing an integer) to a float 92.0.

print(float('36.4'))
# Output: 36.4
# Explanation: Converts the string '36.4' (representing a float) to a float 36.4.

print(float('0075'))
# Output: 75.0
# Explanation: Converts the string '0075' (representing an integer with leading zeros) to a float 75.0. Leading zeros are ignored.

print(float(0B1010101))
# Output: 85.0
# Explanation: Converts the binary literal 0B1010101 (which is 1*64 + 0*32 + 1*16 + 0*8 + 1*4 + 0*2 + 1*1 = 64 + 16 + 4 + 1 = 85) to a float 85.0.

print(float(0O6247))
# Output: 3239.0
# Explanation: Converts the octal literal 0O6247 (which is 6*512 + 2*64 + 4*8 + 7*1 = 3072 + 128 + 32 + 7 = 3239) to a float 3239.0.

print(float(0XA7B9))
# Output: 42937.0
# Explanation: Converts the hexadecimal literal 0XA7B9 (which is 10*4096 + 7*256 + 11*16 + 9*1 = 40960 + 1792 + 176 + 9 = 42937) to a float 42937.0.
'''
print(float(3 + 4j))
# Output: TypeError: float() argument must be a string or a real number, not 'complex'
# Explanation: The `float()` function cannot convert complex numbers directly to floats. It expects real numbers (like integers or other floats) or strings that represent real numbers.

print(float('Ten'))
# Output: ValueError: could not convert string to float: 'Ten'
# Explanation: The `float()` function cannot convert strings that contain non-numeric characters (unless they are valid numeric literals). 'Ten' is not a valid floating-point literal.
'''






