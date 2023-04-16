"""
Write a function that, given a list of words, returns the longest word.
"""

def longer(list):
    """Given a list of words, returns the longest word.

    Args:
        list (String): A list of words (String).

    Returns:
        String: Returns the longest word in the list.
    """
    res = ""
    for i in list:
        if len(i) >= len(res):
            res = i
    
    return res

print(longer(["Hiiiiii", "World"]))
