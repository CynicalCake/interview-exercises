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
    if all_equal(list):
        res = list[0]
    else:
        for i in list:
            if i >= res:
                res = i
    
    return res

def all_equal(list):
    """Recursive function that returns True if all the elements in the list are equal.

    Args:
        list (any): List of any elements.

    Raises:
        Exception: When the list only have one element.

    Returns:
        boolean: True if all the elements in the list are equal, False otherwise.
    """
    res = True
    if len(list) > 2:
        if list[0] != list[1]:
            res = False
        else:
            del list[0]
            res = all_equal(list)
    elif len(list) == 2:
        if list[0] != list[1]:
            res = False
    else:
        raise Exception("The list must have at least 2 elements.")
    
    return res

# print(max_in_list([1, 2, 3, 4, 5]))
