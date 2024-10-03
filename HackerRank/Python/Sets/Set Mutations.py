"""
// The .union() operator returns the union of a set and the set of elements in an iterable. Sometimes, the "|" operator is used in place of .union() operator, but it operates only on the set of elements in set. Set is immutable to the .union() operation (or "|" operation).

You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.

/

// El operador .union() devuelve la unión de un conjunto y el conjunto de elementos en un iterable. A veces, el operador "|" se usa en lugar del operador .union(), pero opera solo en el conjunto de elementos en set. El conjunto es inmutable a la operación .union() (o a la operación "|").

Se le da un conjunto A y N número de otros conjuntos. Este número N de conjuntos tiene que realizar algunas operaciones de mutación específicas en el conjunto A.
Su tarea es ejecutar esas operaciones e imprimir la suma de los elementos del conjunto A.

--------------------------------------------------------------------------------
* Sample Input
16                                             - Size of set A
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52         - All elements in set A
4                                              - Number of operations
intersection_update 10                         - Operation and length of the other set (B)
2 3 5 6 8 9 1 4 7 11                           - Size in the other set (B)
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

? Sample Output
38
--------------------------------------------------------------------------------
"""
_ = int(input())
setA = set(int(x) for x in input().split())

for _ in range(int(input())):
    instruction = list(input().split())
    setB = set(int(x) for x in input().split())

    match instruction[0]:
        case "intersection_update":
            setA.intersection_update(setB)
        
        case "update":
            setA.update(setB)
            
        case "symmetric_difference_update":
            setA.symmetric_difference_update(setB)
            
        case "difference_update":
            setA.difference_update(setB)

print(sum(setA))