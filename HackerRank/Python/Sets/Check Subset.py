"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

/

Se le dan dos conjuntos, A y B.
Su trabajo consiste en averiguar si el conjunto A es un subconjunto del conjunto B.

Si el conjunto A es un subconjunto del conjunto B, imprima True.
Si el conjunto A no es un subconjunto del conjunto B, imprima False.

--------------------------------------------------------------------------------
* Sample Input
3                   - The first line will contain the number of test cases, T
5                   - The first line of each test case contains the number of elements in set A
1 2 3 5 6           - The second line of each test case contains the space separated elements of set A
9                   - The third line of each test case contains the number of elements in set B
9 8 5 6 3 2 1 4 7   - The fourth line of each test case contains the space separated elements of set B
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

? Sample Output
True 
False
False
--------------------------------------------------------------------------------
! Explanation: 
! Set A = {1 2 3 5 6}
! Set B = {9 8 5 6 3 2 1 4 7}
! All the elements of set A are elements of set B. Hence, set A is a subset of set B.
"""
for _ in range(int(input())):
    _ = input()
    A = set(input().split())
    _ = input()
    B = set(input().split())
    
    print(A.issubset(B))