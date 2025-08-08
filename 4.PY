a = 6j
print(a)           # (0+6j)
print(type(a))     # <class 'complex'>
print(a.real)      # 0.0
print(a.imag)      # 6.0
#print(5 + j6)      # Name Error (because `j6` is not valid syntax)
#print(3 + 4i)      # Name Error (Python uses `j`, not `i`)
#print(4 + j)       # Name Error (`j` not defined by itself)
print(4 + 1j)      # (4+1j)
print(4 + 0j)      # (4+0j)