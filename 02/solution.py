text_file = open("/Users/fraser/Projects/advent-of-code/02/input.txt", "r")
input = text_file.readlines()

two_count = 0
three_count = 0

for line in input:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        if line.count(letter) == 2:
            two_count += 1
            break
    for letter in letters:
        if line.count(letter) == 3:
            three_count += 1
            break

print(two_count)
print(three_count)

print(two_count * three_count)

def compare_strings(a, b):
    differences = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            differences += 1
    if differences == 1:
        return a, b
    else:
        return 0, 0

ids = []
for line in input:
    ids.append(line[:-1])

for num in range(len(ids)):
    if num == 0:
        pass
    else:
        check_ids = ids[0:num]
        for check in check_ids:
            a, b = compare_strings(check, ids[num])
            if a != 0:
                print(a)
                print(b)
