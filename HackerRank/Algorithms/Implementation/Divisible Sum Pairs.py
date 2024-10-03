from itertools import combinations

def divisibleSumPairs(k, ar):
    return sum(1 for comb in combinations(ar, 2) if sum(comb) % k == 0)

if __name__ == '__main__':

    _, k = map(int, input().split())

    ar = list(map(int, input().split()))

    result = divisibleSumPairs(k, ar)
    print(result)