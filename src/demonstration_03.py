"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
import re

def string_int(txt):
    '''
    input: str
    output: int

    '''
    # Your code here
    #what to do if there is a letter in the given string - remove all but numbers - check other assignments
    only_nums = re.sub('[^a-zA-Z ]', '', txt)

    return int(only_nums)

# check
print(string_int("65"))
print(string_int("65 tigers"))


