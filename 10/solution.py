import numpy as np
np.set_printoptions(threshold=np.inf)

input = open("/Users/fraser/Projects/advent-of-code/10/input.txt").read().splitlines()

positions = {}
id = 0
extents = []

def get_extent(positions):
    max_y = None
    min_y = None

    for key in positions:
        y = positions[key]['coords'][1]
        if max_y == None or y > max_y:
            max_y = y
        if min_y == None or y < min_y:
            min_y = y

    return max_y - min_y

for line in input:
    # Get rid of initial text
    x = int(line[10:24].split(',')[0])
    y = int(line[10:24].split(',')[1])
    v_x = int(line[36:42].split(',')[0])
    v_y = int(line[36:42].split(',')[1])
    positions[id] = {'coords': [],
                     'velocities': []}
    positions[id]['coords'] = [x, y]
    positions[id]['velocities'] = [v_x, v_y]
    id += 1

extents.append(get_extent(positions))

for i in range(10391):
    for key in positions:
        positions[key]['coords'][0] += positions[key]['velocities'][0]
        positions[key]['coords'][1] += positions[key]['velocities'][1]
    extents.append(get_extent(positions))

print(extents)
print(f'Message aligned at timestep {np.argmin(extents)}')

def show_grid(positions):
    # Work out size of grid
    max_y = None
    min_y = None
    max_x = None
    min_x = None

    for key in positions:
        y = positions[key]['coords'][1]
        if max_y == None or y > max_y:
            max_y = y
        if min_y == None or y < min_y:
            min_y = y
        x = positions[key]['coords'][0]
        if max_x == None or x > max_x:
            max_x = x
        if min_x == None or x < min_x:
            min_x = x

    x_extent = max_x - min_x
    y_extent = max_y - min_y

    print(x_extent)
    print(y_extent)
    print(min_x)
    print(min_y)

    grid = [['.' for x in range(y_extent + 5)] for y in range(x_extent + 5)]

    for key in positions:
        x = positions[key]['coords'][0] - min_x
        y = positions[key]['coords'][1] - min_y
        grid[x][y] = '#'

    for i in grid:
        print(i)
    '''
    for i in range(x_extent + 1):
        grid.append(['.'] * (y_extent + 1))

    for key in positions:
        x = positions[key]['coords'][0] - min_x
        y = positions[key]['coords'][1] - min_y
        grid[x][y] = '#'

    for line in grid:
        print(line)
    '''
show_grid(positions)
