a = True
print(a)               # True — prints the Boolean value
print(type(a))         # <class 'bool'> — `a` is a bool
print(id(a))           # <int> — unique memory address of the `True` singleton

b = False
print(b)               # False — prints the Boolean value
print(type(b))         # <class 'bool'> — `b` is a bool

print(True + True)     # 2 — True is 1, so 1 + 1 = 2 
print(True + False)    # 1 — 1 + 0 = 1 
print(False + True)    # 1 — 0 + 1 = 1 print(False + False)   # 0 — 0 + 0 = 0 
print(True + True + True)   # 3 — 1 + 1 + 1 = 3 

print(25 + 10.8 + True)     # 36.8 — True is 1: 25 + 10.8 + 1 = 36.8

print(True > False)    # True — compares numeric values: 1 > 0

print(True)            # True — prints the Boolean
print(False)           # False — prints the Boolean

#print(true)            # Name Error — `true` is undefined (Python is case‑sensitive)
#print(false)           # Name Error — `false` is undefined (must be capitalized)
