from datetime import datetime

def timeConversion(s):
    # strptime is used to convert the string to datetime object
    # and strftime to format it into a 24-hour string
    return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')

    # # Manually
    #
    # # If date is AM
    # if "AM" in s:
    #     # If the first two digits are 12, change it by 00, otherwise return it with no changes
    #     return "00" + s[2:-2] if s[:2] == "12" else s[:-2]
    #
    # # If date is PM
    # if "PM" in s:
    #     # If the first two digits are 12, return it with no changes, otherwise change it by summing 12
    #     return s[:-2] if s[:2] == "12" else str(int(s[:2]) + 12) + s[2:-2]

if __name__ == '__main__':
    result = timeConversion(input())
    print(result)