def formingMagicSquare(s):
    magic_squares = [
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],

        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],

        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],

        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [8, 3, 4, 1, 5, 9, 6, 7, 2]
    ]
    #   [7, 6, 5, 7, 2, 8, 5, 3, 4]

    # Transform s into a list
    s = [number for row in s for number in row]

    # Calculate and return the minimum cost
    return min(sum(abs(s_i - row_i) for s_i, row_i in zip(s, row)) for row in magic_squares)


if __name__ == '__main__':
    s = [list(map(int, input().split())) for _ in range(3)]

    result = formingMagicSquare(s)
    print(result)