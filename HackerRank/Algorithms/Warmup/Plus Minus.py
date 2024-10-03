def plusMinus(arr):

    # Option 1
    print(f"{sum(1 for i in arr if i > 0) / len(arr):.6f}")
    print(f"{sum(1 for i in arr if i < 0) / len(arr):.6f}")
    print(f"{sum(1 for i in arr if i == 0) / len(arr):.6f}")

    # Option 2
    #
    # plus, minus, zero = (0, 0, 0)
    #
    # for x in arr:
    #     if x > 0:
    #         plus += 1
    #     elif x < 0:
    #         minus += 1
    #     else:
    #         zero += 1
    #
    # print(f"{plus / len(arr):.6f}")
    # print(f"{minus / len(arr):.6f}")
    # print(f"{zero / len(arr):.6f}")


if __name__ == '__main__':

    n = int(input())
    plusMinus(list(map(int, input().split())))






"""
6
-4 -9 0 1 3 4



1 3 4

-4 -9

0


"""