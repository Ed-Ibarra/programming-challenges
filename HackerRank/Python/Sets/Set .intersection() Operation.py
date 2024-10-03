"""
// The ".intersection()" operator returns the intersection of a set and the set of elements in an iterable.
// Sometimes, the & operator is used in place of the ".intersection()" operator, but it only operates on the set of elements in set. The set is immutable to the .intersection() operation (or & operation).

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

/

// El operador ".intersection()" devuelve la intersección de un conjunto y el conjunto de elementos en un iterable.
// A veces, el operador & se usa en lugar del operador ".intersection()", pero solo opera en el conjunto de elementos en set. El conjunto es inmutable a la operación .intersection() (o la operación &).

Los estudiantes del Colegio del Distrito están suscritos a periódicos ingleses y franceses. Algunos estudiantes se han suscrito solo al inglés, otros se han suscrito solo al francés y algunos se han suscrito a ambos periódicos.

Se le dan dos juegos de números de lista de estudiantes. Un grupo se ha suscrito al periódico inglés, otro grupo se ha suscrito al periódico francés. Su tarea es encontrar el número total de estudiantes que se han suscrito a ambos periódicos.
--------------------------------------------------------------------------------
* Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

? Sample Output
5
--------------------------------------------------------------------------------
! Explanation:
! The roll numbers of students who have both subscriptions: 1, 2, 3, 6 and 8.
! Hence, the total is 5 students.

"""
_ = int(input())
setN = set(input().split())
_ = int(input())
setB = set(input().split())

print(len(setB.intersection(setN)))

# setB.intersection(setN) = setB & setN