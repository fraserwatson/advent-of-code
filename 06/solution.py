import numpy as np

input = open("/Users/fraser/Projects/advent-of-code/06/input.txt").read().splitlines()

areas = {}

# Get extent of grid and save coordinates
max_col = 0
max_row = 0
coords = []
for line in input:
    text_coords = line.replace(',', '').split()
    col = int(text_coords[0])
    row = int(text_coords[1])
    coords.append([row, col])
    max_col = max(max_col, col)
    max_row = max(max_row, row)

# Create grid
grid = np.zeros((max_row + 1, max_col + 1))

# Fill grid with ID points
'''
for i in range(len(coords)):
    id = i + 1
    [row, col] = coords[i]
    grid[row, col] = id
'''

# Get total distance for each point

# Add nearest coord to each cell of grid
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        dist = 0
        for coord in coords:
            [row, col] = coord
            dist += abs(row - i) + abs(col - j)
        grid[i, j] = dist

print(len(np.where(grid < 10000)[0]))
