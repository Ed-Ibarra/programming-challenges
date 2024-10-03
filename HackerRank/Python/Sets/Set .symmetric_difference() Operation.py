"""
// The ".symmetric_difference()" operator returns a set with all the elements that are in the set and the iterable but not both.
// Sometimes, a ^ operator is used in place of the ".symmetric_difference()" tool, but it only operates on the set of elements in set.
// The set is immutable to the ".symmetric_difference()" operation (or ^ operation).

Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

/

// El operador ".symmetric_difference()" devuelve un conjunto con todos los elementos que están en el conjunto y el iterable, pero no ambos.
// A veces, se usa un operador ^ en lugar de la herramienta ".symmetric_difference()", pero solo opera en el conjunto de elementos del conjunto.
// El conjunto es inmutable a la operación ".symmetric_difference()" (o a la operación ^).

Los estudiantes del Colegio del Distrito están suscritos a periódicos ingleses y franceses. Algunos estudiantes se han suscrito solo al inglés, otros se han suscrito solo al francés y algunos se han suscrito a ambos periódicos.

Se le dan dos juegos de números de lista de estudiantes. Un grupo se ha suscrito al periódico inglés y otro al periódico francés. Su tarea es encontrar el número total de estudiantes que se han suscrito al periódico en inglés o al francés, pero no a ambos.
--------------------------------------------------------------------------------
* Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

? Sample Output
8
--------------------------------------------------------------------------------
! Explanation:
! The roll numbers of students who have subscriptions to English or French newspapers but not both are:
! 4, 5, 7, 9, 10, 11, 21 and 55.
! Hence, the total is 8 students.

"""
_ = int(input())
setM = set(input().split())
_ = int(input())
setN = set(input().split())

print(len(setM^setN))

# setB.intersection(setN) = setM^setN