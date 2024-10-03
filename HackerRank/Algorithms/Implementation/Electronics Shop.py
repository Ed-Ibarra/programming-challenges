from itertools import product

def getMoneySpent(keyboards, drives, b):

    # Create a list of the sums of all possible combinations without exceeding the budget
    num = [sum(e) for e in sorted(set(product(keyboards, drives))) if sum(e) <= b]

    # If the list is empty, return -1. Otherwise, return the biggest number of the list
    return -1 if num == [] else sorted(num).pop()


if __name__ == '__main__':

    b, n, m = list(map(int, input().split()))

    keyboards = list(map(int, input().split()))
    drives = list(map(int, input().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)