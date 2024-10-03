"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

/

En este desafío, el usuario introduce una cadena y una subcadena. Tiene que imprimir el número de veces que aparece la subcadena en la cadena dada. El recorrido de las cuerdas se llevará a cabo de izquierda a derecha, no de derecha a izquierda.

NOTA: Las letras de cadena distinguen entre mayúsculas y minúsculas.

--------------------------------------------------------------------------------
* Sample Input
ABCDCDC
CDC

? Sample Output
2
--------------------------------------------------------------------------------
! Explanation: Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

"""

# We need to iterate on "string", but first we need to calculate up to which index it will do without having an overflow, that can be achieved by subtracting the length of the "substring" minus 1, to the length of "string".

# Once the iteration limit is set and depending of the length of "substring"(N), we need to take the first N letters from the iteration index and compare them with "substring", so we can apply sum(1) if the comparison is True for each iteration.
def count_substring(string, sub_string):  
    return sum(1 for i in range(len(string) - (len(sub_string)-1)) if string[i:i + len(sub_string)] == sub_string)

if __name__ == '__main__':
    string = input()
    sub_string = input()

    count = count_substring(string, sub_string)
    print(count)