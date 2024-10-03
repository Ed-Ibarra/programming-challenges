def staircase(n):
    # Option 1
    for i in range(1, n+1):
        print( (" "*(n-i)) + ("#"*i) )

    # Option 2
    # [print((" " * (n - i)) + ("#" * i)) for i in range(1, n + 1)]

    # Option 3
    # cont = 1
    # while n > 0:
    #     print(" " * (n - 1) + "#" * cont)
    #     n -= 1
    #     cont += 1

if __name__ == '__main__':

    staircase(int(input()))