"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of "K" members per group where "K" ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear "K" times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of "K" and the room number list.

/

El Sr. Anant Asankhya es el gerente del hotel INFINITE. El hotel cuenta con una infinidad de habitaciones.

Un buen día, un número finito de turistas vienen a alojarse en el hotel.
Los turistas consisten en:
→ Un capitán.
→ Un grupo desconocido de familias que consta de "K" miembros por grupo, donde "K" ≠ 1.

Al Capitán se le dio una habitación separada, y al resto se le dio una habitación por grupo.

El Sr. Anant tiene una lista desordenada de entradas de habitaciones ordenadas al azar. La lista consta de los números de habitación de todos los turistas. Los números de habitación aparecerán "K" veces por grupo, excepto la habitación del capitán.

El Sr. Anant necesita que le ayudes a encontrar el número de la habitación del capitán.
Usted desconoce el número total de turistas o el número total de grupos de familias.
Solo conoce el valor de "K" y la lista de números de habitación.

--------------------------------------------------------------------------------
* Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

? Sample Output
8
--------------------------------------------------------------------------------
! Explanation:
! The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8.
! Hence, 8 is the Captain's room number.

"""
from collections import Counter

_ = int(input())
A = list(int(x) for x in input().split())

# Before you find the minimum, calculate the frequency of each item in list A and use that as a criterion
captain_room = min(Counter(A), key=Counter(A).get)
print(captain_room)