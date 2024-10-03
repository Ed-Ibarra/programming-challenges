def getTotalX(a, b):
    nl = set()
    for i in range(a[-1], b[0] + 1, 1):
        for number in a:
            if i % number == 0 and number == a[-1]:
                nl.add(i)
            elif i % number == 0:
                continue
            else:
                break

    for number in nl:
        # If "all" is True  ->  If every number can divide each item on "b" list
        if all(i % number == 0 for i in b):
            yield number


if __name__ == '__main__':
    _, _ = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = set(getTotalX(a, b))

    print(len(s))