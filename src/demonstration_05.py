"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    """
    Input: List of strings, where all strings might be of different length
    Output: List of strings, where all strings are sorted by length in ASC order
            (Short words first)

    if we are given an empty list, return an empty list

    if two strings have the same length, sort those in alphabetical order

    can we used the built-in 'sort' function?
    """

    #WHAT WE DID - pass in the 'len' function as the 'key' or, pass in an anonymous 
    # lambda function that says to sort by length of each list element

    #from our testing, the BUILT-IN 'sort' method sorts in alphabetical order
    #Sean said lambda is the callback of WEB


    lst.sort(key=lambda x: (len(x), x))
    
    return lst 


    # sort(sort_by_length(lst))


print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
