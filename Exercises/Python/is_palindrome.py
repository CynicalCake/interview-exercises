"""
Write a function that, given a string, returns True if it is a palindrome or False if it is not.
"""

from inverse_string import inverse

def is_palindrome(str):
    """Given a string, returns True if it is a palindrome or False if it is not.

    Args:
        str (string): Any string

    Returns:
        boolean: True if str is palindrome, False if it is not.
    """
    if str.lower() == inverse(str.lower()):
        return True
    return False
    
# print(is_palindrome("radar"))
