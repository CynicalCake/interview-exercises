"""
Write a function that, given a list of integers, prints a histogram to the console.

Example:

input:
[2, 5, 4]

output:
**
*****
****

"""
from generate_characters import repeat_character

def histogram(list):
    """Given a list of integers, prints a histogram to the console.

    Args:
        list (integer): Any list of integers
    """

    for i in list:
        print(repeat_character('*', i))

# histogram([2, 5, 4])
