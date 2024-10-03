"""
Given the names and grades for each student in a class of N students, store
them in a nested list and print the name(s) of any student(s) having the 
second lowest grade.

Note: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.

--------------------------------------------------------------------------------
* Sample Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

? Sample Output
Berry
Harry
--------------------------------------------------------------------------------
! Explanation: There are 5 students in this class whose names and grades are
! assembled to build the following list...
! [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
! The lowest grade of 37.2 belongs to Tina. The second lowest grade of
! 37.21 belongs to both Harry and Berry, so we order their names alphabetically
! and print each name on a new line.
"""

lst = []
set_A = set()

# 2 variables are created, "lst" will be a list of lists with the names and
# its respective grades and "set_A" will be a set with every unique grade
for i in range(int(input())):
    lst.append([input(), float(input())])
    set_A.add(lst[i][1])

# "lst" is sort to print the names alphabetically if there are 2 or more matches
lst.sort()

# Loop through "lst" and print the name if their grade matches the second
# lowest in "set_A" (sorted from lowest to highest)
for position in range(len(lst)):
    if lst[position][1] == sorted(set_A)[1]:
        print(lst[position][0])