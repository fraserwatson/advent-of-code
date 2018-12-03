text_file = open("/Users/fraser/Projects/advent-of-code/01/input.txt", "r")
input = text_file.readlines()

def find_value(input):
    total = 0
    list_of_values = set()
    while True:
        for line in input:
            symbol = line[0]
            value = int(line[1:-1])
            if symbol == '+':
                total += value
            else:
                total -= value
            if total in list_of_values:
                return total
            else:
                list_of_values.add(total)

print(find_value(input))
