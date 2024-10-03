"""
In this challenge, you will be given 2 integers, n and m. 

There are n words, which might repeat, in word group A. 
There are m words belonging to word group B.

For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. 

If it does not appear, print -1.

--------------------------------------------------------------------------------
* Sample Input
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

? Sample Output
1 2 4
3 5
--------------------------------------------------------------------------------
! Explanation:
! 'a' appeared 3 times in positions 1, 2 and 4.
! 'b' appeared 2 times in positions 3 and 5.
! In the sample problem, if 'c' also appeared in word group B, you would print -1.
"""
from collections import defaultdict

group_A, group_B = map(int, input().split())

default_dictionary = defaultdict(list)

# For loop will be used to simulate the position of each entry,
# when a duplicate appears it just add its position in the "default_dictionary"
for i in range(1, group_A + 1):
    default_dictionary[input()].append(i)  # => {'a': [1, 2, 4], 'b': [3, 5]})

# Search every input in the defaultdict, print its indices if exist, or -1 if don't
for _ in range(group_B):
    print(*default_dictionary.get(input()) or [-1])