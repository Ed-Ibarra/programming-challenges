import textwrap

def wrap(string, max_width):
    # Option 1
    #
    # Text width
    tw = textwrap.TextWrapper(width=max_width)

    # Text dedent
    dedent = textwrap.dedent(text=string)

    lines = tw.fill(text=dedent)

    return lines


    # Option 2
    # return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)