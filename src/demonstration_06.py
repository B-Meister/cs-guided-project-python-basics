"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True - 2x 2o
- XO("xooxx") ➞ False - 3x 2o
- XO("ooxXm") ➞ True (Case insensitive) - 2o 2x
- XO("zpzpzpp") ➞ True (Returns True if no x and o) - 0x 0o
- XO("zzoo") ➞ False - 0x 2o
"""
def XO(txt):
    # Your code here
    """
    input: a random string (may or may not contain x's and o's)
    output: boolean - is there the same number of x's and o's

    Casing doesn't matter, treat capital and lowercase x's and o's as the same

    When we walked through the example in our head, we physically counter the
    # of x's and # of o's. If they matched = True, if not = False
    """
    #resets the count to 0
    o_count = 0
    x_count = 0

    # we need to make this logic case-INsensitive
    txt.lower() #put everything in the same case - no need to output the original txt

    for char in txt.lower():
        if char == "o":
            o_count += 1
        if char == "x":
            x_count += 1
        else: 
            pass
    
    return o_count == x_count

#check 
print (XO("ooxx")) #true
print (XO("xooxx")) #false
print (XO("ooxXm")) #true
print (XO("zpzpzpp")) #true
print (XO("zzoo")) #false




