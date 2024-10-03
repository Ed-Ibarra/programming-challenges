"""
In this task, we would like for you to appreciate the usefulness of the
groupby() function of itertools.

You are given a string S. Suppose a character 'c' occurs consecutively X times
in the string. 

Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

--------------------------------------------------------------------------------
* Sample Input
1222311

? Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
--------------------------------------------------------------------------------
! Explanation: 
! First, the character 1 occurs only once. It's replaced by (1, 1). Then the
! character 2 occurs three times, and it is replaced by (3, 2) and so on. 
! Also, note the single space within each compression and between the compressions.
"""
from itertools import groupby

# groupby will group each similar character until find out a different one
# The variable "number" will represent the first character that was found
# "lst" will store all the same characters until the disruption, but it will
# need to be casted into a list to get their data
for number, lst in groupby(input()):
    print(f"({len(list(lst))}, {number})", end=" ")