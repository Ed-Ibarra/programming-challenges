def dayOfProgrammer(year):
    if year >= 1919:
        print(f"12.09.{year}" if is_leap(year) else f"13.09.{year}")
    elif year == 1918:
        print(f"26.09.{year}")
    else:
        print(f"12.09.{year}" if year % 4 == 0 else f"13.09.{year}")

def is_leap(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

if __name__ == '__main__':
    dayOfProgrammer(int(input()))