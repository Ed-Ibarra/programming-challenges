def sockMerchant(ar):
    lst = list(set(ar)) # [10, 20, 50, 30]

    return sum(arr.count(x) // 2 for x in lst)

if __name__ == '__main__':

    _ = int(input())
    arr = list(map(int, input().split()))

    result = sockMerchant(arr)
    print(result)