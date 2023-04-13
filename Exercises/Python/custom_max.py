"""
Write a function that returns the larger of two numbers.
"""

def custom_max(n1, n2):
    """Given two numbers, the larger of them is returned.

    Args:
        n1 (integer): First number
        n2 (integer): Second number
    Returns:
        integer: The larger of both numbers.
    """

    if n1 < n2:
        return n2
    elif n2 < n1:
        return n1
    elif n1 == n2:
        raise Exception("The entered values are the same.")
    raise Exception("Something went wrong.")

# print (custom_max(200, 100))
