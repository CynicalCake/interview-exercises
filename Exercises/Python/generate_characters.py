"""
Write a function that, given a character and an integer n, returns the character n times.
"""

def repeat_character(char, n):
    """Given a character and an integer n, returns n times the character.

    Args:
        char (char): Any character
        n (integer): The times the user wants the character to repeat
    """

    repeated_char = ""
    for i in range(n):
        repeated_char = repeated_char + char

    return repeated_char

# print(repeat_character('x', 10))
