a=3247
print(a)               # 3247 
pa = 0O6247
print(type(a))         # <class 'int'> 
print(id(a))           # <int> 

b = 0o6247
print(id(b))           # <int> 
print(b)               # 3247 

c = 3239
print(c)               # 3239 
print(id(c))           # <int> 

#print(0o9248)          # Syntax Error  digits 8 and 9 not allowed


a = 0XA7B9
print(a)             # 42937 — hex A7B9 equals decimal 42937
print(type(a))       # <class 'int'> — hex literal is an integer

b = 0xBEEF
print(b)             # 48879 — hex BEEF equals decimal 48879

#print(A7B9)          # Name Error — A7B9 is not a defined variable

print('A7B9')        # A7B9 — prints the string as-is
'''
print(0XBEER)        # Syntax Error — ‘R’ is not a valid hex digit (only 0–9, A–F) 

print(0XHYD)         # Syntax Error — ‘H’, ‘Y’, ‘D’ are invalid hex digits 

print(0xA7G9B)       # Syntax Error — ‘G’ is not a valid hex digit 

'''