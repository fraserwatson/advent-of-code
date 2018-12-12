input = open("/Users/fraser/Projects/advent-of-code/12/input.txt").read().splitlines()

n_generations = 10000

initial_state = '..' * n_generations + input[0].split()[2] + '..' * n_generations

conditions = {}
n_pots = len(input[0].split()[2])
state = initial_state

pot_indices = [i for i in range(0 - (2*n_generations), n_pots + (2*n_generations))]

# For each condition line
for i in range(2, len(input)):
    key = input[i][:5]
    val = input[i][9]
    conditions[key] = val

for i in range(1, n_generations + 1):
    #print(i)
    number_of_pots = len(pot_indices)

    # Initialize new pot states
    new_state = '..'

    # Check each pot
    for pot in range(2, number_of_pots-2):
        local_env = state[pot-2:pot+3]
        if local_env in conditions:
            new_state += conditions[local_env]
        else:
            #print('SHOULD NOT BE HERE')
            new_state += '.'
    new_state += '..'
    state = new_state
    if i % 1000 == 0:
        total = 0
        for s, character in enumerate(state):
            if character == '#':
                #print(pot_indices[i])
                total += pot_indices[s]
        print(str(i) + ': ' + str(total))

    #print(str(i) + ': ' + state)
'''
total = 0

for s, character in enumerate(state):
    if character == '#':
        #print(pot_indices[i])
        total += pot_indices[s]

#print(pot_indices)
#print(state)
print(total)
'''
