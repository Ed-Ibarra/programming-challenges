def diagonalDifference(arr):

    d1 = sum(arr[i][i] for i in range(len(arr)))
    d2 = sum(arr[len(arr) - 1 - i][i] for i in range(len(arr)))

    # Option 1
    #
    # Sum the diagonal from left to right
    # d1 = sum(arr[i][i] for i in range(len(arr)))
    # # Sum the diagonal from left to right
    # d2 = sum(arr[abs(i-(len(arr)-1))][i] for i in range(len(arr)-1, -1, -1))
    return abs(d1 - d2)


    # Option 2
    #
    # d1 = sum(arr[i][i] for i in range(len(arr)))
    # d2 = sum(arr[len(arr) - 1 - i][i] for i in range(len(arr)))


    # Option 2
    #
    # return abs(sum(arr[i][i] for i in range(len(arr))) - sum(arr[abs(i-(len(arr)-1))][i] for i in range(len(arr)-1, -1, -1)))



    # Option 3
    #
    # i, j, s1, s2 = 0, len(arr) - 1, 0, 0
    #
    # for row in arr:
    #     s1 = s1 + row[i]
    #     i += 1
    #     s2 = s2 + row[j]
    #     j -= 1
    #
    # return (abs(s1 - s2))


if __name__ == '__main__':

    arr = [list(map(int, input().split())) for _ in range(int(input()))]
    print(diagonalDifference(arr))