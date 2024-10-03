"""
They're combinations allowing the individual elements to be repeated more than once
                    AA
                    AB
    A,B,C :2  ->    AC
                    BB
                    BC
                    CC
                    
You are given a string S. Your task is to print all possible size k replacement
combinations of the string in lexicographic sorted order.

--------------------------------------------------------------------------------
* Sample Input
HACK 2

? Sample Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
--------------------------------------------------------------------------------
"""
from itertools import combinations_with_replacement

text, number = input().split()
combinations = combinations_with_replacement(sorted(text), int(number))

# Sorting the product of "combinations" and print its join
for permutation in sorted(combinations):
    print("".join(permutation))