"""
Let's use decorators to build a name directory!

You are given some information about N people. Each person has a first name,
last name, age and sex.

Print their names in a specific format sorted by their age in ascending order
i.e. the youngest person's name should be printed first.

For two people of the same age, print them in the order of their input.

--------------------------------------------------------------------------------
* Sample Input
3
Mike Thomson 20 M
Robert Bustle 32 M
Andrea Bustle 30 F

? Sample Output
Mr. Mike Thomson
Ms. Andrea Bustle
Mr. Robert Bustle
--------------------------------------------------------------------------------
"""
def person_lister(function):
    
    def inner_func(people):
        # Sorts "people" by the 3rd column and then passes its content 1 by 1 to outer function
        for person in sorted(people, key=lambda x: int(x[2])):
            yield function(person)

    # This is for execute the inner function
    return inner_func

# The wrapper function is executed first and next function is passed as parameter
@person_lister
def name_format(person):
    return f"{("Mr." if person[3] == "M" else "Ms.")} {person[0]} {person[1]}"

if __name__ == '__main__':
    
    n = int(input())
    people = [input().split() for i in range(n)]
    
    print(*name_format(people), sep='\n')