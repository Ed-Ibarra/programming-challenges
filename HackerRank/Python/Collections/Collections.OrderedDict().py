"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each "item_name" and "net_price" in order of its first occurrence.

--------------------------------------------------------------------------------
* Sample Input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

? Sample Output
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
--------------------------------------------------------------------------------
! Explanation:
! BANANA FRIES: Quantity bought: 1, Price: 12
! Net Price: 12
! POTATO CHIPS: Quantity bought: 2, Price: 30
! Net Price: 60
! APPLE JUICE: Quantity bought: 2, Price: 10
! Net Price: 20
! CANDY: Quantity bought: 4, Price: 5
! Net Price: 20
"""
from collections import OrderedDict

items = int(input())
purchases_list = [input().split() for _ in range(items)]

# In every input of "purchases_list", the last position has the net_price.
# So, we have to loop through the whole list and access to it with [-1]
net_price = [int(purchases_list[i][-1]) for i in range(items)]

# After of create a new list of the net_price, we can delete the last position
# for every input of "purchases_list" and join the rest. 
# That way in "purchases_list" we splitted item_name from net_price
for i in range(items):
    purchases_list[i].pop()
    purchases_list[i] = " ".join(purchases_list[i])

purchases_dictionary = OrderedDict()

for i in range(items):
    # If the entry in "purchases_list" does not exist in the dictionary, it'll
    # be added with its respective operation (net_price * item_quantity),
    # that way we will avoid unnecessary operations and save time.
    # purchases_dictionary = {"name_1": (net_price * item_quantity), "name_2": (net_price * item_quantity),...}
    if purchases_list[i] not in purchases_dictionary:
        purchases_dictionary[purchases_list[i]] = net_price[i]*purchases_list.count((purchases_list[i]))

for key, value in purchases_dictionary.items():
    print(f"{key} {value}", sep="\n")