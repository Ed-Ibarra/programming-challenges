def gradingStudents(grades):
    for score in grades:
        if score < 38 or (5 - score%5) >= 3:
            yield score
        else:
            yield score + (5 - score%5)

if __name__ == '__main__':
    grades = []

    for _ in range(int(input())):
        grades.append(int(input()))

    print(*gradingStudents(grades), sep="\n")