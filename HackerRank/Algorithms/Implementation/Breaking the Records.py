def breakingRecords(scores):
    min, max = scores[0], scores[0]
    m, M = 0, 0

    for i in range(len(scores)):
        if scores[i] < min:
            m += 1
            min = scores[i]

        if scores[i] > max:
            M += 1
            max = scores[i]

    return M, m


if __name__ == '__main__':
    _ = int(input())
    scores = list(map(int, input().split()))
    result = breakingRecords(scores)
    print(*result)



"""

9
10 5 20 20 4 5 2 25 1

"""