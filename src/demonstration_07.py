"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1 (1st smallest = 1)
- nth_smallest([1, 3, 5, 7], 3) ➞ 5 (3rd smallest = 5)
- nth_smallest([1, 3, 5, 7], 5) ➞ None (5th smallest = only have 4 elements)
- nth_smallest([7, 3, 5, 1], 2) ➞ 3 (2nd smallest = 3)
"""
def nth_smallest(lst, n):
    # Your code here
    """
    input: List of unsorted ints
    output: int, the nth smallest int in the list

    If the input is sorted in ascending order, we can then simply return 
    the nth element from the sorted list

    What does 'built-in' sort do to the list

    """
#making sure that the user is asking for something that we can give
    #if number is greater than length
    if n > len(lst):
        return "There are not enough variables in the list to return the {}th smallest element".format(n)
    #if number is less than length
    if n <= 0:
        return "Please input a positive integer that is within the length of the list"
    
     # sort the list of numbers in ascending order
    lst.sort()
    return lst[n-1]


#check - change the n-variable
print(nth_smallest([7, 5, 3, 1], 3))
print(nth_smallest([7, 5, 3, 1], -2))
print(nth_smallest([7, 5, 3, 1], 8))
