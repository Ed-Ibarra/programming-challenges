def pickingNumbers(a, n):
    s = []

    if len(set(a)) == 1:
        return n

    for i in range(n):
        for j in range(n):
            if i != j and abs(a[i] - a[j]) == 1:
                s.append(a.count(a[i]) + a.count(a[j]))
                break
            elif i != j and abs(a[i] - a[j]) == 0:
                s.append(a.count(a[i]))
                break

    return max(s)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    result = pickingNumbers(a, n)
    print(result)




"""

6
4 6 5 3 3 1

[1, 3, 3, 4, 5, 6]




73
4 2 3 4 4 9 98 98 3 3 3 4 2 98 1 98 98 1 1 4 98 2 98 3 9 9 3 1 4 1 98 9 9 2 9 4 2 2 9 98 4 98 1 3 4 9 1 98 98 4 2 3 98 98 1 99 9 98 98 3 98 98 4 98 2 98 4 2 1 1 9 2 4



100
4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97

"""