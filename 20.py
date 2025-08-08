print(oct(195))
# Output: 0o303
# Explanation: Converts the decimal integer 195 to its octal representation.
# Reading remainders from bottom to top: 303. 

print(oct(0B10101110010))
# Output: 0o2562
# Explanation: First, 0B10101110010 is a binary literal. Python converts this binary number to an integer internally, then `oct()` converts that integer to its octal string representation.
# Binary to Decimal: 1*1024 + 0*512 + 1*256 + 0*128 + 1*64 + 1*32 + 1*16 + 0*8 + 0*4 + 1*2 + 0*1 = 1024 + 256 + 64 + 32 + 16 + 2 = 1394
# Reading remainders from bottom to top: 2562.

print(oct(0xA7B9))
# Output: 0o123671
# Explanation: First, 0xA7B9 is a hexadecimal literal. Python converts this hexadecimal number to an integer internally, then `oct()` converts that integer to its octal string representation.
# Hexadecimal to Decimal: A=10, B=11
# 10*4096 + 7*256 + 11*16 + 9*1 = 40960 + 1792 + 176 + 9 = 42937
# Reading remainders from bottom to top: 123671. 


