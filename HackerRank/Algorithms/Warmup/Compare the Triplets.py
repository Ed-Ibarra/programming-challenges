import time
def compareTriplets(a, b):

    As = sum(1 for i in range(3) if a[i] > b[i])
    Bs = sum(1 for i in range(3) if a[i] < b[i])

    return As, Bs

if __name__ == '__main__':

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = compareTriplets(a, b)

    print(*result)


# def measure_time():
#     start_time = time.time()
#     # Here it goes the function
#     end_time = time.time()
#     print(end_time - start_time)