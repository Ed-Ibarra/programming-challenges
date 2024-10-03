"""
It refers to the arrangement of all or some elements of a set in a specific order
The order of the elements is important. Know how many different ways we can sort
                    ABC
                    ACB
    A,B,C :3  ->    BAC
                    BCA
                    CAB
                    CBA
                    
You are given a string S. Your task is to print all possible permutations of
size "k" of the string in lexicographic sorted order.

--------------------------------------------------------------------------------
* Sample Input
HACK 2

? Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
--------------------------------------------------------------------------------
"""
from itertools import permutations

text, number = input().split()

# Sorting the product of "permutations" function and print its join
for permutation in sorted(permutations(text, int(number))):
    print("".join(permutation))