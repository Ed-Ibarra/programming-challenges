def merge_the_tools(s, k):

    # Option 1
    for i in range(0, len(s), k):
        # dict.fromkeys() creates a dictionary based on every unique element of each substring, then we print them
        print(''.join(dict.fromkeys(s[i:i + k])))

    # Option 2
    #
    # for i in range(0, len(s), k):
    #     unique = ""
    #     for letter in s[i:i + k]:
    #         if letter not in unique:
    #             unique += letter
    #     print(unique)


if __name__ == '__main__':
    merge_the_tools(input(), int(input()))