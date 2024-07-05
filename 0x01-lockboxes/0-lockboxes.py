#!/usr/bin/python3
"""
Solution to lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    
    Args:
        boxes (list of list of int): A list where each index represents a box containing keys to other boxes.
    
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not isinstance(boxes, list):
        return False
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0].copy()

    while keys:
        new_key = keys.pop()
        if 0 <= new_key < n and not unlocked[new_key]:
            unlocked[new_key] = True
            keys.extend(boxes[new_key])

    return all(unlocked)
    