"""
Write a function sum() and mult() that respectively add and multiply all the numbers in a list.
"""

def custom_sum(list):
    """Given a list, returns the sum of all elements of the list.

    Args:
        list (integers, decimals): An array of integers or decimals.

    Returns:
        integer, decimal: The sum of all elements of the array.
    """

    res = 0
    for i in list:
        res = res + i
    return res

def custom_mult(list):
    """Given a list, returns the multiplication of all the elements of the list.

    Args:
        list (integers, decimals): An array of integers or decimals.

    Returns:
        integer, decimal: The multiplication of all elements of the array.
    """
    res = 1
    for i in list:
        res = res * i
    return res

# print(custom_sum([1, 2, 3, 4, 5]))
# print(custom_mult([1, 2, 3, 4, 5]))
