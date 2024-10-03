"""
Combinations focus on the selection of elements from a set regardless of order.
The order of the elements is NOT important. Know how many different ways we can sort
                    AB
    A,B,C :2  ->    AC          AB = BA
                    BC

You are given a string s. Your task is to print all possible combinations, 
up to size k, of the string in lexicographic sorted order.

--------------------------------------------------------------------------------
* Sample Input
HACK 2

? Sample Output
A
C
H
K
AC
AH
AK
CH
CK
HK
--------------------------------------------------------------------------------
"""
from itertools import combinations

text, number = input().split()

"""
Since the expected output also contains individual characters, we need to set
the first "for loop" to change the "range" that will be needed as a parameter
to print each ordered combination
"""
for i in range(1, int(number) + 1):
    for permutation in sorted(combinations(sorted(text), i)):
        print("".join(permutation))