print(bool(0))
# Output: False
# Explanation: The integer 0 is considered falsy.

print(bool(10))
# Output: True
# Explanation: The integer 10 is a non-zero number, hence considered truthy.

print(bool(-25))
# Output: True
# Explanation: The integer -25 is a non-zero number, hence considered truthy.

print(bool(0.0))
# Output: False
# Explanation: The float 0.0 is considered falsy.

print(bool(0.1))
# Output: True
# Explanation: The float 0.1 is a non-zero number, hence considered truthy.

print(bool(0 + 0j))
# Output: False
# Explanation: A complex number where both the real and imaginary parts are zero is considered falsy.

print(bool(10 + 20j))
# Output: True
# Explanation: A complex number is considered truthy if either its real part or its imaginary part (or both) are non-zero. Here, both are non-zero.

print(bool(-15j))
# Output: True
# Explanation: A complex number with a non-zero imaginary part (-15) is considered truthy, even if the real part is implicitly zero.

print(bool('False'))
# Output: True
# Explanation: This is a non-empty string. Any non-empty string, regardless of its content, is considered truthy.

print(bool(''))
# Output: False
# Explanation: An empty string is considered falsy.

print(bool('Hyd'))
# Output: True
# Explanation: This is a non-empty string, hence considered truthy.

print(bool(' '))
# Output: True
# Explanation: This is a non-empty string (it contains a space character), hence considered truthy.

print(bool('True'))
# Output: True
# Explanation: This is a non-empty string, hence considered truthy.












