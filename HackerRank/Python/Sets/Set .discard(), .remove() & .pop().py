"""
// The operation ".remove(x)" removes element x from the set. If element x does not exist, it raises a KeyError.

// ".discard(x)" operation also removes element x from the set. If element x does not exist, it does not raise a KeyError.

You have a non-empty set "s", and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

/

// La operación ".remove(x)" elimina el elemento x del conjunto. Si el elemento x no existe, genera un KeyError.

// La operación ".discard(x)" también elimina el elemento x del conjunto. Si el elemento x no existe, no genera un KeyError.

Tiene un conjunto "s" no vacío y tiene que ejecutar N comandos dados en N líneas.

Los comandos serán pop, remove y discard.

--------------------------------------------------------------------------------
* Sample Input
9                       - The first line contains size of "s"
1 2 3 4 5 6 7 8 9       - The second line contains all of the elements are non-negative integers, less than or equal to 9
10                      - The third line contains the number of commands.
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

? Sample Output
4
--------------------------------------------------------------------------------
! Explanation: After completing these 10 operations on the set, we get set([4]). Hence, the sum is 4.
! Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.
"""
_ = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
        
    match command[0]:
        
        case "pop":
            s.pop()
            
        case "remove":
            s.remove(int(command[1]))
        
        case "discard":
            s.discard(int(command[1]))

print(sum(s))