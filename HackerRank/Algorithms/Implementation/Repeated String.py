def repeatedString(s, n):
    # Return 0 if there is not any "a" on the string
    if "a" not in s:
        return 0
    # If the string is just an "a", return n itself
    elif (len(s) == 1):
        return n
    # If there is an "a" in the string and is greater than 1
    else:
        # If "n" is a multiple of "len(s)"
        if n % len(s) == 0:
            # Multiply the number of a's in the original string by the
            # dvision of "n" by the length of "s"
            return s.count("a") * (n//len(s))
        # If "n" is not a multiple of "len(s)",
        else:
            # Multiply the number of a's in the original string by the
            # dvision of "n" by the length of "s", then you can sum it how many
            # a's there are in the rest of the imaginary string
            return (s.count("a") * (n//len(s))) + (s[:n % len(s)].count("a"))


    # All of the options below may issues with too many longs requests

    # Option 2
    #
    # return (s * (n // len(s) + 1))[:n].count("a") if len(s) != 1 or "a" not in s else n

    # Option 3
    #
    # if len(s) != 1 or "a" not in s:
    #     return (s * (n // len(s) + 1))[:n].count("a")
    # else:
    #     return n

    # Option 4
    #
    # if len(s) == 1 and s == "a":
    #     return n
    #
    # s = (s * n)[0:n]
    #
    # return (s.count("a"))



if __name__ == '__main__':

    result = repeatedString(input(), int(input()))

    print(result)


"""

cilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlangcilusdhvbufysbvskudbisulbibdiablanrglanhilarnghnahlgibhalirgnhislnhlang
1848627681682551

abcac
15

"""