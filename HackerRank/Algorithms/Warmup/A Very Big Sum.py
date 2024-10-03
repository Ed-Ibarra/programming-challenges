def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    _ = int(input())

    result = aVeryBigSum(list(map(int, input().split())))
    print(result)