#!/usr/bin/python3
"""Compute the perimeter of a grid
"""

def island_perimeter(grid):
    """Compute the perimeter of a grid.
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume all sides are surrounded by water

                # Check neighboring cells, subtract perimeter for adjacent land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract left side
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract top side

    return perimeter

