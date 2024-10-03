def birthday(s, day, month):
    if len(s) == 1:
        return 1 if s[0] == day else 0

    else:
        pieces = []
        # For 0 until N
        for i in range(len(s) - month + 1):
            # Add segments of M digits, depending by month's value
            pieces.append([s[i+j] for j in range(month)])

        return sum(1 for x in pieces if sum(x) == day)


if __name__ == '__main__':

    _ = int(input())
    s = list(map(int, input().split()))

    day, month = map(int, input().split())
    result = birthday(s, day, month)

    print(result)


"""

19
2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1
18 7

S = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]

day = 18
month = 7

2, 5, 1, 3, 4, 4, 3
5, 1, 3, 4, 4, 3, 5
1, 3, 4, 4, 3, 5, 1


1
4
4 1



S = [4]

day = 4
month = 1





13
4 5 4 2 4 5 2 3 2 1 1 5 4
15 4


S = [4, 5, 4, 2, 4, 5, 2, 3, 2, 1, 1, 5, 4]

day = 15
month = 4

4 5 4 2     ->  15
5 4 2 4     ->  15
4 2 4 5     ->  15
2 4 5 2     ->  13
4 5 2 3     ->  14
5 2 3 2     ->  12
2 3 2 1     ->  8
3 2 1 1     ->  7
2 1 1 5     ->  9
1 1 5 4     ->  11

"""