"""
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks,
class and name. Your task is to help Dr. Wesley calculate the average marks
of the students.

Average = Sum of all marks / Total students

Note:
1. Columns can be in any order. IDs, marks, class and name can be written
in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME.
--------------------------------------------------------------------------------
* Sample Input
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

? Sample Output
78.00
--------------------------------------------------------------------------------
! Explanation: Average = (97 + 50 + 91 + 72 + 80) / 5 = 78.00
"""
from collections import namedtuple

students_number = int(input())
titles = namedtuple('Student', input().split())
sum_marks = 0

# Sum every values from the "MARKS" title and get the average
for _ in range(students_number):
    sum_marks += int(titles(*input().split()).MARKS)

average = sum_marks/students_number

print(f"{average:.2f}")