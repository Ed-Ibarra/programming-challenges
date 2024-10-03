"""
Given the participants' score sheet for your University Sports Day, you are
required to find the runner-up score. You are given N scores. Store them in 
a list and find the score of the runner-up.

--------------------------------------------------------------------------------
* Sample Input
5
2 3 6 6 5

? Sample Output
5
--------------------------------------------------------------------------------
! Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second 
! maximum is 5. Hence, we print 5 as the runner-up score.
"""

_ = int(input())

scores = set(map(int, input().split()))
print(sorted(scores)[-2])