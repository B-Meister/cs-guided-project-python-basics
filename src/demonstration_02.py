"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes):
    '''
    input: int (minutes)
    output: int (seconds)

    We know there are 60 seconds in each minute

    What do we do if negative? - Still must give the number of seconds because might be counting down
    '''
    seconds = abs(minutes) * 60

    return seconds

print(convert(3))
print(convert(-5))
