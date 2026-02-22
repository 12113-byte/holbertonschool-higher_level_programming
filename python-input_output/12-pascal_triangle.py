#!/usr/bin/python3
"""Pascal's triangle generator"""


def pascal_triangle(n):
    """Returns a list of lists, representing Pascal's triangle of n rows"""

    if n <= 0:
        return []

    triangle = [[1]]  # this is the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # very first element

        # middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)  # very last element
            triangle.append(row)

    return triangle
