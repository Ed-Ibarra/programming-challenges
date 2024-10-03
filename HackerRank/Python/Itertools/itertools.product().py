"""
It refers to the possible combinations
                    AC
    A,B ->          AD
    C,D             BC
                    BD
                    
You are given a two lists A and B. Your task is to compute their Cartesian product AxB

--------------------------------------------------------------------------------
* Sample Input
1 2
3 4

? Sample Output
(1, 3) (1, 4) (2, 3) (2, 4)
--------------------------------------------------------------------------------
"""
from itertools import product

A = map(int, input().split())
B = map(int, input().split())

print(type(A))
print(A)

# Sorting the product of "product" function and print its join
for each in sorted(set(product(A,B))):
    print(each, end=" ")