a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May be'}

print(a)
# Output: {True: 'May be'}  (or sometimes {1: 'May be'})
# Explanation: Dictionaries store only unique keys. In Python, the hash values of `True`, `1`, and `1.0` are all the same.
# - The first key-value pair `{True: 'Yes'}` is added.
# - When `{1: 'No'}` is added, the key `1` is considered a duplicate of `True`, and its value is updated to `'No'`.
# - When `{1.0: 'May be'}` is added, the key `1.0` is also considered a duplicate, and the value is again updated to `'May be'`.
# The final dictionary contains only one key-value pair with the last assigned value.

print(len(a))
# Output: 1
# Explanation: The length of the dictionary is the number of unique keys, which is 1.


