print(int(10.8))
# Output: 10
# Explanation: Converts the float 10.8 to an integer by truncating the decimal part.

print(int(True))
# Output: 1
# Explanation: Converts the boolean True to its integer equivalent, which is 1.

print(int(False))
# Output: 0
# Explanation: Converts the boolean False to its integer equivalent, which is 0.

print(int('25'))
# Output: 25
# Explanation: Converts the string '25' into an integer 25.

print(int('0075'))
# Output: 75
# Explanation: Converts the string '0075' into an integer 75. Leading zeros are ignored.

print(int(0B11010))
# Output: 26
# Explanation: Converts the binary literal 0B11010 (which is 1*16 + 1*8 + 0*4 + 1*2 + 0*1 = 26) to an integer.

print(0B11010)
# Output: 26
# Explanation: This directly prints the integer value of the binary literal 0B11010.

print(int(0O6247))
# Output: 3239
# Explanation: Converts the octal literal 0O6247 (which is 6*512 + 2*64 + 4*8 + 7*1 = 3072 + 128 + 32 + 7 = 3239) to an integer.

print(0O6247)
# Output: 3239
# Explanation: This directly prints the integer value of the octal literal 0O6247.

print(int(0XA7B9))
# Output: 42937
# Explanation: Converts the hexadecimal literal 0XA7B9 (which is 10*4096 + 7*256 + 11*16 + 9*1 = 40960 + 1792 + 176 + 9 = 42937) to an integer. (A=10, B=11)

print(0XA7B9)
# Output: 42937
# Explanation: This directly prints the integer value of the hexadecimal literal 0XA7B9.

#print(int(3 + 4j))
# Output: TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# Explanation: The `int()` function cannot convert complex numbers directly to integers. It expects real numbers (like floats or integers) or strings that represent integers.

#print(int('25.4'))
# Output: ValueError: invalid literal for int() with base 10: '25.4'
# Explanation: The `int()` function can only convert strings that represent whole numbers. 

#print(int('Ten'))
# Output: ValueError: invalid literal for int() with base 10: 'Ten'
# Explanation: The `int()` function cannot convert strings that contain non-numeric characters


