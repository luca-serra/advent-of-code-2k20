def get_adjacent_occupied_seats(grid, i, j):
    """
    Given the row index i and the column index j of a sead on the grid,
    return the number of adjacent occupied seats among the 8 adjacent seats.
    grid is a list of string characters, symbolizing the seat occupations.
    """
    m = len(grid)
    n = len(grid[0])

    if i == 0:
        row_indices = [0, 1]
    elif i == m - 1:
        row_indices = [m - 2, m - 1]
    else:
        row_indices = [i - 1, i, i + 1]

    if j == 0:
        column_indices = [0, 1]
    elif j == n - 1:
        column_indices = [n - 2, n - 1]
    else:
        column_indices = [j - 1, j, j + 1]

    adjacent_occupied_seats = 0
    for u in row_indices:
        for v in column_indices:
            if (u, v) != (i, j) and grid[u][v] == "#":
                adjacent_occupied_seats += 1

    return adjacent_occupied_seats


def get_adjacent_occupied_seats_extended(grid, i, j):
    """
    Given the row index i and the column index j of a sead on the grid,
    return the number of adjacent occupied seats, following the extended rule (part 2).
    grid is a list of string characters, symbolizing the seat occupations.
    """
    m = len(grid)
    n = len(grid[0])

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    adjacent_occupied_seats = 0

    for direction in directions:
        r_idx, c_idx = i + direction[0], j + direction[1]
        while r_idx in list(range(m)) and c_idx in list(range(n)):
            if grid[r_idx][c_idx] == "#":
                adjacent_occupied_seats += 1
                break
            elif grid[r_idx][c_idx] == "L":
                break
            r_idx += direction[0]
            c_idx += direction[1]

    return adjacent_occupied_seats


def count_occupied_seats(grid):
    """Return the number of occupied seats in a grid"""
    count = 0
    for seats in grid:
        for seat in seats:
            if seat == "#":
                count += 1
    return count
