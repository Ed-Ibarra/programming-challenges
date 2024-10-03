def libraryFine(d1, m1, y1, d2, m2, y2):
    # The book was returned after the due year -> fine = 10,000
    if y1 > y2:
        return 10000
    # Within of the same year, the book was returned months after due date -> fine = (number of months late) * 500
    elif y1 == y2 and m1 > m2:
        return ((m1 - m2) * 500)
    # Within of the same year and month, the book was returned after the due day -> fine = (number of days late) * 15
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return ((d1 - d2) * 15)
    # Any other option gives 0
    else:
        return 0


if __name__ == '__main__':

    # Get the day, month, and year on which the book was returned
    d1, m1, y1 = map(int, input().split())

    # Get the day, month, and year on which the book was due to be returned
    d2, m2, y2 = map(int, input().split())

    # Print the result
    print(libraryFine(d1, m1, y1, d2, m2, y2))