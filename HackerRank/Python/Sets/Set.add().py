"""
// If we want to add a single element to an existing set, we can use the .add() operation. It adds the element to the set and returns 'None'.

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

/

// Si queremos agregar un solo elemento a un conjunto existente, podemos usar la operación .add(). Agrega el elemento al conjunto y devuelve 'None'.

Aplica tus conocimientos sobre la operación .add() para ayudar a tu amigo Rupal.

Rupal tiene una gran colección de sellos del país. Decidió contar el número total de sellos de distintos países en su colección. Ella pidió tu ayuda. Seleccionas los sellos uno por uno de una pila de sellos de N países.

Encuentre el número total de sellos de distintos países.

--------------------------------------------------------------------------------
* Sample Input
7
UK
China
USA
France
New Zealand
UK
France

? Sample Output
5
--------------------------------------------------------------------------------
! Explanation: UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).

"""
countries = set()

for _ in range(int(input())):
    countries.add(input())

print(len(countries))