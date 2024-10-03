"""
You are given a function f(X) = X^2. You are also given K lists.
The i^th list consists of N(i^th) elements

S = ( f(X1) + f(X2) + ... + f(Xk) ) % M

Xi denotes the element picked from the i^th list.
Find the maximized value S(max) obtained.

Note that you need to take exactly one element from each list, not necessarily
the largest element. You add the squares of the chosen elements and perform the
modulo operation.

The maximum value that you can obtain, will be the answer to the problem.

--------------------------------------------------------------------------------
* Sample Input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

? Sample Output
206
--------------------------------------------------------------------------------
! Explanation: 
! Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list
! gives the maximum S value equal to
! (5^2 + 9^2 + 10^2) % 1000 = 206
"""
import itertools

list_size, modulo = map(int, input().split())

combinations_list = []
results = []

# Save inputs one-by-one, delete the first digit due is the size of the input
for _ in range(list_size):
    local_list = list(map(int, input().split()))
    del local_list[0]
    combinations_list.append(local_list)

combinations_list = list(itertools.product(*combinations_list))

# Prints the highest value of each result of each combination -> (a^2 + b^2 + c^2 + ... + n^2) % M
for combination in combinations_list:
    results.append(sum(permutation**2 for permutation in combination) % modulo)
    
print(max(results))