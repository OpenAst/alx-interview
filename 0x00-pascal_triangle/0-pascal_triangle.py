#!/usr/bin/python3
"""
@n- an integer
Return - list or 0 if n<= 0
"""

def pascal_triangle(n):
    """
    a function that retrns pascal triangle
    """
    if n <= 0:
        return []
    else:
        triangle  = [[1]]
        for i in range(1, n):
            prev_row = triangle[-1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j]
            new_row.append(10
                triangle.append(1)
                triangle.append(new_row)
        return triangle
