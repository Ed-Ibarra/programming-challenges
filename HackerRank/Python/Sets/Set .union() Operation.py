"""
// The .union() operator returns the union of a set and the set of elements in an iterable. Sometimes, the "|" operator is used in place of .union() operator, but it operates only on the set of elements in set. Set is immutable to the .union() operation (or "|" operation).

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

/

// El operador .union() devuelve la unión de un conjunto y el conjunto de elementos en un iterable. A veces, el operador "|" se usa en lugar del operador .union(), pero opera solo en el conjunto de elementos en set. El conjunto es inmutable a la operación .union() (o a la operación "|").

Los estudiantes del Colegio del Distrito están suscritos a periódicos ingleses y franceses. Algunos estudiantes se han suscrito solo al inglés, otros se han suscrito solo al francés y algunos se han suscrito a ambos periódicos.

Se le dan dos juegos de números de lista de estudiantes. Un conjunto está suscrito al periódico inglés y el otro conjunto está suscrito al periódico francés. El mismo estudiante podría estar en ambos conjuntos. Su tarea es encontrar el número total de estudiantes que se han suscrito al menos a un periódico.

--------------------------------------------------------------------------------
* Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

? Sample Output
13
--------------------------------------------------------------------------------
! Explanation:
! Roll numbers of students who have at least one subscription:
! 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21 and 55. Roll numbers: 1, 2, 3, 6 and 8 are in both sets so they are only counted once.
! Hence, the total is 13 students.
"""
_ = int(input())
setN= set(input().split())
_ = int(input())
setB = set(input().split())

print(len(setB.union(setN)))

# setB.union(setN)) = setB | setN