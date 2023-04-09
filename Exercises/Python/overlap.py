"""
Write an overlap() function that, given two lists, returns True if they have at least 1 member in common, or False otherwise.
THE FUNCTION MUST BE WRITtEN USING A NESTED FOR LOOP.
"""

def overlap(list1, list2):
    """Given two lists, returns True if they have at least 1 member in common, or False otherwise.

    Args:
        list1 (any): First list
        list2 (any): Second list

    Returns:
        boolean: True if there is an element of list1, or False if there is not.
    """

    for elem1 in list1:
        for elem2 in list2:
            if elem1 == elem2:
                return True
    
    return False

# print(overlap([1,2,3], [3,4,5]))
