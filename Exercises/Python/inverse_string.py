"""
Write a function that returns the inverse of a string.
"""

def inverse(str):
    """Given a string, returns the same string but inverted.

    Args:
        str (string): Any string

    Returns:
        string: Inverted string
    """

    inverted_string = ""
    for char in str:
        inverted_string = char + inverted_string
    return inverted_string

# print(inverse("Hello World!"))
