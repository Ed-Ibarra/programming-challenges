"""
Mike is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay  amount of money only
if they get the shoe of their desired size.

Your task is to compute how much money Mike earned.
--------------------------------------------------------------------------------
// The first line contains X, the number of shoes.
// The second line contains the space separated list of all the shoe sizes in the shop.
// The third line contains N, the number of customers.
// The next N lines contain the space separated values of the shoe size desired by the customer and i, the price of the shoe.
* Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

? Sample Output
200
--------------------------------------------------------------------------------
! Explanation:
! Customer 1: Purchased size 6 shoe for $55.
! Customer 2: Purchased size 6 shoe for $45.
! Customer 3: Size 6 no longer available, so no purchase.
! Customer 4: Purchased size 4 shoe for $40.
! Customer 5: Purchased size 18 shoe for $60.
! Customer 6: Size 10 not available, so no purchase.
! Total money earned = 55 + 45 + 40 + 60 = $200 
"""
from collections import Counter

_ = int(input())
shoe_sizes = map(int, input().split())
customers_number = int(input())
sales = 0
counter_shoe_sizes = Counter(shoe_sizes)

# Shoes size desired and the price willing to pay of every customer
customer_request = [list(map(int, input().split())) for _ in range(customers_number)]

# Search the shoes size for each request and if exist, 
# sale it and remove the size of the Counter object
for i in range(customers_number):
    if counter_shoe_sizes[customer_request[i][0]]:
        sales += customer_request[i][1]
        counter_shoe_sizes[customer_request[i][0]] -= 1

print(sales)