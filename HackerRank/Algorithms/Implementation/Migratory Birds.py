def migratoryBirds(arr):
    lst = list(set(arr))
    k = []

    for i in lst:
        # Append the times what each unique number appears on lst
        k.append(arr.count(i))

    # max(k) -> first max number on the lst    k.index() -> index of the first max number on the lst
    return lst[k.index(max(k))]

if __name__ == '__main__':
    arr_count = int(input())

    result = migratoryBirds(list(map(int, input().split())))
    print(result)