"""
Let's dive into decorators!
You are given N mobile numbers. Sort them in ascending order then print them
in the standard format shown below: +91 xxxxx xxxxx.

The given mobile numbers may have +91, 91 or 0 written before the actual 10
digit number. Alternatively, there may not be any prefix at all.

--------------------------------------------------------------------------------
* Sample Input
3
07895462130
919875641230
9195969878

? Sample Output
+91 78954 62130
+91 91959 69878
+91 98756 41230
--------------------------------------------------------------------------------
"""

def wrapper(function):
    def inner_func(lst):
        lst = sorted([int(number[-10:]) for number in lst])
        function([f"+91 {str(number)[:5]} {str(number)[5:]}" for number in lst])

    return inner_func


@wrapper
# The wrapper function is executed first and next function is passed as parameter
def sort_phone(lst):
    print(*sorted(lst), sep='\n')


if __name__ == '__main__':
    lst = [input() for _ in range(int(input()))]
    sort_phone(lst)