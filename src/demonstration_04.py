"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length, width):
    """
    Insert Documentation here - 

    """

    if length <= 0 or width <= 0:
        return 0
    else:
        #computing the perimeter once we NEED to 
        #so that computational power is not wasted if not needed
        perimeter = (length + width) * 2
        
        return perimeter

#check from examples - for python repl
print(find_perimeter(6, 7))
print(find_perimeter(20, 10))
print(find_perimeter(2, 9))
print(find_perimeter(-5, 4))

