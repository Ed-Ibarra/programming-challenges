def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    result = split_and_join(input())
    print(result)