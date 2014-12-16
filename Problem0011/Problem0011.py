from numpy import matrix
from operator import mul


def euler():
    # Convert the grid in the text file into a list of lists analogous to a matrix that I can iterate through easily
    f = open("Problem0011supp")

    grid = []
    for line in f:
        grid = grid + [map(int, (line[:-1].split(" ")))]

    max_value = 0;
    # Iterate and check forward through the list, taking into account boundary conditions
    # Only check in the S, E, NE, SE directions because this covers all combinations
    rows = len(grid)
    cols = len(grid[1])
    for row in range(0, rows):
        for col in range(0, cols):

            # Check S direction, don't do it if within 3 of the bottom boundary
            if row <= rows - 4:
                value = grid[row][col] * grid[row + 1][col] * grid[row + 2][col] * grid[row + 3][col]
                if value > max_value:
                    max_value = value

            # Check E direction, don't do it if within 3 of the right boundary
            if col <= cols - 4:
                value = grid[row][col] * grid[row][col + 1] * grid[row][col + 2] * grid[row][col + 3]
                if value > max_value:
                    max_value = value

            # Check NE direction don't do it if within 3 of the top and/or right boundaries
            if col <= cols - 4 and row >= 3:
                value = grid[row][col] * grid[row - 1][col + 1] * grid[row - 2][col + 2] * grid[row - 3][col + 3]
                if value > max_value:
                    max_value = value

            # Check SE direction, don't do it if within 3 of the bottom and/or right boundaries
            if col < cols - 4 and row <= rows - 4:
                value = grid[row][col] * grid[row + 1][col + 1] * grid[row + 2][col + 2] * grid[row + 3][col + 3]
                if value > max_value:
                    max_value = value

    print max_value

euler()