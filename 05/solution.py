alphabet = 'abcdefghijklmnopqrstuvwxyz'

def length_of_chain(input, unit_to_remove):
    current_chain_length = len(input)
    while True:
        for i in range(1, len(input)):
            first_letter = input[i-1]
            last_letter = input[i]
            lower_first_letter = first_letter.lower()
            upper_first_letter = first_letter.upper()
            if (first_letter == lower_first_letter and last_letter == upper_first_letter) or (first_letter == upper_first_letter and last_letter == lower_first_letter):
                input = input[0:i-1] + input[i+1:]
                current_chain_length = len(input)
                break
            if i == (len(input)-1):
                return current_chain_length

input = open("/Users/fraser/Projects/advent-of-code/05/input.txt").read().splitlines()[0]
shortest_chain_length = len(input)

for letter in alphabet:
    print(letter)
    input = open("/Users/fraser/Projects/advent-of-code/05/input.txt").read().splitlines()[0]
    input = input.replace(letter, '')
    input = input.replace(letter.upper(), '')
    chain_length = length_of_chain(input, letter)
    print(chain_length)
    if chain_length < shortest_chain_length:
        shortest_chain_length = chain_length

print(shortest_chain_length)
