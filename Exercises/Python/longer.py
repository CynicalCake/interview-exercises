"""
Write a function that, given a list of words, returns the longest word.
"""

def longer(list):
    res = ""
    for i in list:
        if len(i) >= len(res):
            res = i
    
    return res

print(longer(["Hiiiiii", "World"]))
