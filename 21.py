print(hex(25))
# Output: 0x19
# Explanation: Converts the decimal integer 25 to its hexadecimal representation.
# Reading remainders from bottom to top: 19.

print(hex(0B10101111010111))
# Output: 0x2bd7
# Explanation: First, 0B10101111010111 is a binary literal. Python converts this binary number to an integer internally, then `hex()` converts that integer to its hexadecimal string representation.
# Binary to Decimal:
# 1 * 8192 + 0 * 4096 + 1 * 2048 + 0 * 1024 + 1 * 512 + 1 * 256 + 1 * 128 + 1 * 64 + 0 * 32 + 1 * 16 + 0 * 8 + 1 * 4 + 1 * 2 + 1 * 1
# = 8192 + 2048 + 512 + 256 + 128 + 64 + 16 + 4 + 2 + 1 = 11223
# Reading remainders from bottom to top: 2BD7.

print(hex(0O6247))
# Output: 0xca7
# Explanation: First, 0O6247 is an octal literal. Python converts this octal number to an integer internally, then `hex()` converts that integer to its hexadecimal string representation.
# Octal to Decimal:
# 6*512 + 2*64 + 4*8 + 7*1 = 3072 + 128 + 32 + 7 = 3239
# Reading remainders from bottom to top: CA7.

