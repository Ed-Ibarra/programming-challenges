"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

/

Dados 2 conjuntos de números enteros, M y N, imprime su diferencia simétrica en orden ascendente. El término diferencia simétrica indica aquellos valores que existen en M o N pero que no existen en ambos.

--------------------------------------------------------------------------------
* Sample Input
4
2 4 5 9
4
2 4 11 12

? Sample Output
5
9
11
12
--------------------------------------------------------------------------------

"""
_ = int(input())
M = set(input().split())
_ = int(input())
N = set(input().split())

# First we get the symmetric difference between both sets and order the result, then we print each element per line
[print(item) for item in sorted([int(x) for x in M.symmetric_difference(N)])]