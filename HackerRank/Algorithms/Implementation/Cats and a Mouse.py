def catAndMouse(x, y, z):
    if abs(z-y) == abs(z-x):
        return "Mouse C"
    elif abs(z-y) < abs(z-x):
        return "Cat B"
    else:
        return "Cat A"

if __name__ == '__main__':

    for _ in range(int(input())):
        x, y, z = map(int, input().split())
        result = catAndMouse(x, y, z)
        print(result)