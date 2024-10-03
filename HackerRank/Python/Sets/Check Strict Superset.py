"""
You are given a set A and N other sets. Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

/

Se le da un conjunto A y otros N conjuntos. Su trabajo consiste en averiguar si el conjunto A es un super conjunto
estricto de cada uno de los N conjuntos.

Print True, si A es un super conjunto estricto de cada uno de los N conjuntos. De lo contrario, imprima False.
Un super conjunto estricto tiene al menos un elemento que no existe en su subconjunto.
--------------------------------------------------------------------------------
* Sample Input
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

? Sample Output
False
--------------------------------------------------------------------------------
! Explanation:
! Set A is the strict superset of the set ([1, 2, 3, 4, 5]) but not of the set ([100, 11, 12]) because 100 is not in set A.
! Hence, the output is False.
"""
def isstrictsuperset(A, b):
    # True -> If all the elements of the set "b" exist in "A" AND if "A" is not a subset of "b"
    return b.issubset(A) and not (A.issubset(b))

if __name__ == '__main__':
    A = set(int(x) for x in input().split())
    res = True

    for _ in range(int(input())):
        b = set(int(x) for x in input().split())

        # "res" always will start as True boolean, but as we call the function that checks if set b is in set A, we will check that if its value was changed to "false". If this happens, we will get out of the loop
        res &= isstrictsuperset(A, b)
        if res == False:
            break

    print(res)