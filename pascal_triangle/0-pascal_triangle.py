#!/usr/bin/python3
"""
Module 0-pascal_triangle
Define a fonction pascal's triangle
"""


def pascal_triangle(n):
    """
    Create a list of list in integers in Pascal's triangle.
    Args:
        n (int): the number of lines of triangle.
    Returns:
        list: a list dof lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]

        for j in range(1, i):
            val = prev_row[j - 1] + prev_row[j]
            current_row.append(val)

        current_row.append(1)
        triangle.append(current_row)

    return triangle
