"""
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed below. Iterate through each
command in order and perform the corresponding operation in its list.

1. insert i e: At position i insert integer e
2. print: Print the list
3. remove e: Delete the first occurrence of integer e
4. append e: Insert integer e at the end of the list
5. sort: Sort the list
6. pop: Pop the last element from the list
7. reverse: Reverse the list

--------------------------------------------------------------------------------
* Sample Input
4
append 1
append 2
insert 1 3
print

? Sample Output
[1, 3, 2]
--------------------------------------------------------------------------------
! Explanation:
! append 1 -> arr = [1]
! append 2 -> arr = [1, 2]
! insert 3 1 -> arr = [1, 3, 2]

"""

n = int(input())
lst = []

for _ in range(n):
    
    command, *numbers = input().split()
    numbers = [int(number) for number in numbers]
    
    if command == 'print':
        print(lst)
    else:
        # Here, "lst" and "command" are used to create a temporary function
        # that will use the "numbers" list content of unpacked way, thus
        # avoiding writing too many "if" conditions
        temporary_function = getattr(lst, command)
        temporary_function(*numbers)