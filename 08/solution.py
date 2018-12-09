input = open("/Users/fraser/Projects/advent-of-code/08/input.txt").read().split()

input = list(map(int, input))

def get_checksum(input):
    total = 0
    nodes = input.pop(0)
    entries = input.pop(0)

    print(f'Nodes: {nodes}')
    print(f'Entries: {entries}')
    #print(f'Input: {input}')

    for i in range(nodes):
        total += get_checksum(input)

    for i in range(entries):
        total += input.pop(0)

    return total

#total = get_checksum(input)

node_name = ord('A') - 1

def get_node_value(input):

    global node_name
    node_name += 1
    total = 0
    nodes = input.pop(0)
    metadata = input.pop(0)
    child_node_values = []
    elements = []

    print(f'Name of node: {chr(node_name)}')
    print(f'Child nodes: {nodes}')
    print(f'Metadata elements: {metadata}')

    if nodes == 0:
        for i in range(metadata):
            total += input.pop(0)
        print(f'Total: {total}')
    else:
        for i in range(nodes):
            child_node_values.append(get_node_value(input))
        for i in range(metadata):
            elements.append(input.pop(0))
        for element in elements:
            if element == 0 or element > len(child_node_values):
                pass
            else:
                print(element)
                print(child_node_values)
                total += child_node_values[element-1]

    return total

total = get_node_value(input)
print(total)
