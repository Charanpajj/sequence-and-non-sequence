a = 'Sankar Dayal Sarma'

print(a[7 : 12])
# Output: Daya
# Explanation: Slices from index 7 (inclusive 'D') up to, but not including, index 12 ('l'). So, 'Dayal'.

print(a[7 : ])
# Output: Dayal Sarma
# Explanation: Slices from index 7 (inclusive 'D') to the end of the string.

print(a[ : 6])
# Output: Sankar
# Explanation: Slices from the beginning of the string (index 0) up to, but not including, index 6 (the space).

print(a[ : ])
# Output: Sankar Dayal Sarma
# Explanation: Slices from the beginning to the end, with a step of 1 (default). This creates a full copy of the string. Equivalent to a[0:18:1].

print(a[: : ])
# Output: Sankar Dayal Sarma
# Explanation: Same as a[:], slices from the beginning to the end with the default step of 1.

print(a[1 : 10 : 2])
# Output: aanDya
# Explanation: Slices from index 1 ('a') up to, but not including, index 10 ('a'), taking every 2nd character.
# Indices: 1 (a), 3 (k), 5 (r), 7 (D), 9 (a)

print(a[0 : : 2])
# Output: SakrDylSm
# Explanation: Slices from index 0 to the end, taking every 2nd character.
# Indices: 0(S), 2(n), 4(a), 6( ), 8(a), 10(y), 12( ), 14(a), 16(r) -> 'Sankar Dayal Sarma'

print(a[1 : : 2])
# Output: an a ara
# Explanation: Slices from index 1 to the end, taking every 2nd character.
# Indices: 1(a), 3(k), 5(r), 7(D), 9(a), 11(l), 13(S), 15(r), 17(a) -> 'Sankar Dayal Sarma'

print(a[-5 : -1])
# Output: Sarm
# Explanation: Slices from index -5 (inclusive 'S') up to, but not including, index -1 ('a').

print(a[::-1])
# Output: amraS layaD raknaS
# Explanation: Slices the entire string in reverse order (step of -1).

print(a[-1:-5:-1])
# Output: amra
# Explanation: Slices from index -1 (inclusive 'a') down to, but not including, index -5 ('S'), with a step of -1.
# Characters are a(-1), m(-2), r(-3), a(-4).

print(a[ : : -2])
# Output: amSlyDknS
# Explanation: Slices the entire string in reverse order, taking every second character.

print(a[3 : -3])
# Output: kar Dayal Sar
# Explanation: Slices from index 3 (inclusive 'k') up to, but not including, index -3 ('r').
# Characters included: k(3), a(4), r(5), (6), D(7), a(8), y(9), a(10), l(11), (12), S(13), a(14), r(15).

print(a[2 : -5])
# Output: nkar Dayal S
# Explanation: Slices from index 2 (inclusive 'n') up to, but not including, index -5 ('S').
# Characters included: n(2), k(3), a(4), r(5), (6), D(7), a(8), y(9), a(10), l(11), (12), S(13).

print(a[-1:-5])
# Output: (empty string)
# Explanation: When slicing with a positive step (default 1), if the start index is greater than or equal to the stop index, an empty string is returned. Here, -1 is effectively "after" -5 when moving forward, so it results in an empty slice.

print(a[3 : 3])
# Output: (empty string)
# Explanation: When the start index is equal to the stop index, an empty string is returned because the slice range is exclusive of the stop index.
