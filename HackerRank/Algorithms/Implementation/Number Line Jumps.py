def kangaroo(x1, v1, x2, v2):
    # If any of these are true, return "NO":
    #   - Start position and jump distance for kangaroo 1 is lower than kangaroo 2
    #   - Start position and jump distance for kangaroo 2 is lower than kangaroo 1
    if (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2) or (v1 == v2 and x1 != x2):
        return ("NO")

    elif x1 < x2:
        while True:
            print(x1, x2)
            x1 += v1
            x2 += v2

            if x1 == x2:
                return ("YES")
            elif x1 > x2:
                return ("NO")
    elif x2 < x1:
        while True:
            x1 += v1
            x2 += v2
            if x1 == x2:
                return ("YES")
            elif x1 > x2:
                return ("NO")


"""
x1 v1   x2 v2
21  6   47 3
27 50
33 53
39 56
45 59
51 62
57 65
63 68
69 71
75 74
81 77
"""



    # if x1 < x2:
    #     while 1:
    #         x1 = x1 + v1
    #         x2 = x2 + v2
    #
    #         if x1 == x2:
    #             return ("YES")
    #         elif x1 > x2:
    #             return ("NO")
    #
    # if x1 > x2:
    #     while 1:
    #         x1 = x1 + v1
    #         x2 = x2 + v2
    #
    #         if x1 == x2:
    #             return ("YES")
    #         elif x1 < x2:
    #             return ("NO")
    #
    # return ("YES")


if __name__ == '__main__':

    values = list(map(int, input().split()))

    result = kangaroo(*values)

    print(result)