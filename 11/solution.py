input = 9221

import numpy as np

grid = np.zeros((300,300))

for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        x_coord = x + 1
        y_coord = y + 1
        power_level = 0

        rack_id = x_coord + 10
        power_level = rack_id * y_coord
        power_level += input
        power_level *= rack_id
        if power_level > 99:
            str_power_level = str(power_level)
            power_level = int(str_power_level[-3])
        else:
            power_level = 0
        power_level -= 5
        grid[x, y] = power_level

max_cell_power = -1e9
top_left_x = 0
top_left_y = 0
max_size_of_square = 300
square_size_for_solution = 0

for x in range(grid.shape[0]):
    for y in range(grid.shape[0]):
        cell_power = grid[x, y]
        for size in range(2, max_size_of_square):
            if x + size > max_size_of_square or y + size > max_size_of_square:
                pass
            else:
                x_line = size + x - 1
                y_line = size + y - 1
                cell_power = cell_power + sum(grid[x_line, y:y_line]) + sum(grid[x:x_line, y_line]) + grid[x_line, y_line]
                if cell_power > max_cell_power:
                    max_cell_power = cell_power
                    top_left_x = x + 1
                    top_left_y = y + 1
                    square_size_for_solution = size
        print(f'Coords: {x}, {y}   Max power: {max_cell_power}   Max coords: {top_left_x}, {top_left_y}   Square size: {square_size_for_solution}')
