def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':

    candles_count = int(input())
    candles = list(map(int, input().split()))

    print(birthdayCakeCandles(candles))