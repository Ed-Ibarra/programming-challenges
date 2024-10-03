def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

    # Option 2
    #
    # # Transform string into a list
    # l = list(string)
    # # Insert character on desired position
    # l[position] = character
    # # Return the list as string
    # return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)