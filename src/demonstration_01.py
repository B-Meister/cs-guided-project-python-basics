"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""
def addition(a, b):
    """
    input: 2 ints
    output: 1 int
    """
    sum = a + b
    return sum

#test/check
print(addition(3,7)) #output should be 10
print(addition(-6,13)) #output should be 7
print(addition(9,0)) #output should be 9
