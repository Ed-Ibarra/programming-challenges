"""
The included code stub will read an integer, n, from STDIN. Without using
any string methods, try to print the following: 123...n

Note that "..." represents the consecutive values in between.

--------------------------------------------------------------------------------
* Sample Input
3

? Sample Output
123
--------------------------------------------------------------------------------
"""

for i in range(int(input())):
    print(i + 1, end="")