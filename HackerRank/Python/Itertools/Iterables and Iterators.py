"""
You are given a list of N lowercase English letters. For a given integer K,
you can select any K indices (assume 1-based indexing) with a uniform 
probability from the list.

Find the probability that at least one of the K indices selected will contain
the letter: 'a'.

--------------------------------------------------------------------------------
* Sample Input
4 
a a c d
2

? Sample Output
0.8333
--------------------------------------------------------------------------------
! Explanation:
! All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
! (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)

! Out of these 6 combinations, 5 of them contain either index 1 or index 2 
! which are the indices that contain the letter 'a'.

! Hence, the answer is 5/6 -> 0.833.

"""
from itertools import combinations


_ = int(input())
letters = input().split()
number_of_indexes = int(input())
index_combination = [*combinations(letters, number_of_indexes)]

# The times that "a" appears in every combination
a_appears = (sum(1 for pair in index_combination if pair.count("a") > 0))

# Probability of found an "a" in all possible combinations
print(a_appears / len(index_combination))