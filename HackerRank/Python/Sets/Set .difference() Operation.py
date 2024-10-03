"""
// The tool .difference() returns a set with all the elements from the set that are not in an iterable. Sometimes the "-" operator is used in place of the .difference() tool, but it only operates on the set of elements in set. Set is immutable to the .difference() operation (or the - operation).

Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

/

// La herramienta .difference() devuelve un conjunto con todos los elementos del conjunto que no están en un iterable. A veces, el operador "-" se usa en lugar de la herramienta .difference(), pero solo opera en el conjunto de elementos del conjunto. El conjunto es inmutable a la operación .difference() (o a la operación -).

Los estudiantes del Colegio del Distrito están suscritos a los periódicos en inglés y francés. Algunos estudiantes se han suscrito solo al periódico en inglés, algunos se han suscrito solo al periódico en francés y algunos se han suscrito a ambos periódicos.

Se le dan dos juegos de números de lista de estudiantes. Un grupo se ha suscrito al periódico inglés y otro al periódico francés. Su tarea es encontrar el número total de estudiantes que se han suscrito solo a periódicos en inglés.
--------------------------------------------------------------------------------
* Sample Input
* The first line contains the number of students who have subscribed to the English newspaper.
* The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
* The third line contains the number of students who have subscribed to the French newspaper.
* The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

? Sample Output
4
--------------------------------------------------------------------------------
! Explanation:
! The roll numbers of students who only have English newspaper subscriptions are: 4, 5, 7 and 9.
! Hence, the total is 4 students.

"""
_ = int(input())
setM = set(input().split())
_ = int(input())
setN = set(input().split())

print(len(setM - setN))

# setM.difference(setN) = setM - setN