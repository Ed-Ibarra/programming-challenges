def countingValleys(steps, path):
    valley, cont = 0, 0
    in_valley = False

    for step in path:
        cont += 1 if step == "U" else -1

        if cont <= -1 and in_valley == False:
            in_valley = True
            valley += 1

        elif cont >= 0 and in_valley:
            in_valley = False

    return valley


if __name__ == '__main__':
    result = countingValleys(int(input()), input())
    print(result)