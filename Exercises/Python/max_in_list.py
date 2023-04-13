"""
Write a function that, given a list of numbers, returns the largest.
"""

def max_in_list(list):
    """Given a list of numbers, returns the largest.

    Args:
        list (any number): List of numbers.

    Returns:
        any number: The largest number on the list.
    """
    res = 0
    for i in list:
        if i >= res:
            res = i
    
    return res

# print(max_in_list([1, 2, 3, 4, 5]))
