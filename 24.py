r = range(10 , 17 , 3)

a , b , c = r
print(a , b , c)
# Output: 10 13 16
# Explanation: The 'range' object 'r' contains three elements (10, 13, 16). The variables 'a', 'b', and 'c' are assigned to these elements in order, and the `print()` function displays their values.

r = range(3)

#x , y = r
# Output: Value Error: too many values to unpack (expected 2)
# Explanation: The 'range' object 'r' now contains three elements (0, 1, 2). The assignment statement tries to unpack these three elements into only two variables ('x' and 'y'). Since the number of elements does not match the number of variables, a `Value Error` is raised.

#p , q , r , s = r
# Output: Value Error: not enough values to unpack (expected 4, got 3)
# Explanation: The 'range' object 'r' contains three elements (0, 1, 2). The assignment statement tries to unpack these into four variables ('p', 'q', 'r', 's'). Since there are not enough elements to fill all the variables, a `Value Error` is raised.

#a , b , c = *r
# Output: Syntax Error: can't use starred expression here
# Explanation: The starred expression `*r` cannot be used on the right-hand side of a simple assignment statement in this manner. The correct way to unpack a sequence like `range` is `a, b, c = r` without the `*`. This is a `Syntax Error` and would prevent the program from running.

