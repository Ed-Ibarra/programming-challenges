"""
The provided code stub will read in a dictionary containing key/value pairs of
name:[marks] for a list of students. Print the average of the marks array for
the student name provided, showing 2 places after the decimal.

--------------------------------------------------------------------------------
* Sample Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

? Sample Output
56.00
--------------------------------------------------------------------------------
! Explanation: Marks for Malika are {52, 56, 60} whose average is (52+56+60)/3 -> 56
"""

student_marks = {}

for _ in range(int(input())):
    name, *scores = input().split()
    scores = list(map(float, scores))
    student_marks[name] = scores  # Dictionary Format → name: [scores]

query_name = input()

""" Search the query_name in the dictionary """
if query_name in student_marks.keys():
    # Get the average of their marks and print it with 2 decimals
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")