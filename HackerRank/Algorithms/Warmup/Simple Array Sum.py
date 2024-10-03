def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':

    _ = int(input().strip())

    result = simpleArraySum(map(int, input().split()))

    print(result)