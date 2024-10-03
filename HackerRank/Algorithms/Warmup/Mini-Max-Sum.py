def miniMaxSum(arr):
    # Option 1
    print(sum(arr)-max(arr), sum(arr)-min(arr))

    # Option 2
    # print(min([(sum(arr) - i) for i in arr]), end=" ")
    # print(max([(sum(arr) - i) for i in arr]))

    # Option 3
    # print(min([(sum(arr) - i) for i in arr]), max([(sum(arr) - i) for i in arr]))

    # Option 4
    # m = min([(sum(arr) - i) for i in arr])
    # M = max([(sum(arr) - i) for i in arr])
    # print(m, M)

    # Option 5
    # storage = 0
    # suma = sum(arr)
    # new_list = []
    #
    # for x in arr:
    #     storage = suma - x
    #     new_list.append(storage)
    #
    # print(min(new_list), max(new_list))


if __name__ == '__main__':
    miniMaxSum(list(map(int, input().split())))