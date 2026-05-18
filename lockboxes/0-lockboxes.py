#!/usr/bin/python3
"""
Module to solve the lockboxes puzzle.
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Each box is numbered sequentially from 0 to n - 1 and each box
    may contain keys to the other boxes.

    Args:
        boxes (list of list): A list of lists representing boxes and keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    total_boxes = len(boxes)
    opened_boxes = {0}

    boxes_to_check = [0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()
        for key in boxes[current_box]:
            if key < total_boxes and key not in opened_boxes:
                opened_boxes.add(key)
                boxes_to_check.append(key)

    return len(opened_boxes) == total_boxes
