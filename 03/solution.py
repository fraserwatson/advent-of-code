import numpy as np

text_file = open("/Users/fraser/Projects/advent-of-code/03/input.txt", "r")
input = text_file.readlines()

max_width = 0
max_height = 0
list_of_ids = []

for line in input:
    split_line = line.split()
    list_of_ids.append(split_line[0])
    margins = split_line[2]
    l_margin = int(margins.split(',')[0])
    t_margin = int(margins.split(',')[1][:-1])
    dims = split_line[3]
    xdim = int(dims.split('x')[0])
    ydim = int(dims.split('x')[1])
    width = l_margin + xdim
    height = t_margin + ydim
    if width > max_width:
        max_width = width
    if height > max_height:
        max_height = height

fabric = np.zeros((max_height + 1, max_width + 1))

for line in input:
    split_line = line.split()
    id = split_line[0]
    margins = split_line[2]
    l_margin = int(margins.split(',')[0])
    t_margin = int(margins.split(',')[1][:-1])
    dims = split_line[3]
    xdim = int(dims.split('x')[0])
    ydim = int(dims.split('x')[1])
    for row in range(ydim):
        for col in range(xdim):
            fabric[t_margin + row, l_margin + col] += 1

for line in input:
    split_line = line.split()
    id = split_line[0]
    margins = split_line[2]
    l_margin = int(margins.split(',')[0])
    t_margin = int(margins.split(',')[1][:-1])
    dims = split_line[3]
    xdim = int(dims.split('x')[0])
    ydim = int(dims.split('x')[1])
    use_for_suit = True
    for row in range(ydim):
        for col in range(xdim):
            if fabric[t_margin + row, l_margin + col] > 1:
                use_for_suit = False
    if use_for_suit:
        print(id)



print(fabric)
print((fabric > 1).sum())
