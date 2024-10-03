def bonAppetit(bill, k, b):
    brian = bill[k]
    bill.remove(brian)

    bill = sum(bill) // 2

    return "Bon Appetit" if b - bill == 0 else b - bill


if __name__ == '__main__':
    n, k = map(int, input().split())

    bill = list(map(int, input().split()))
    b = int(input())

    print(bonAppetit(bill, k, b))