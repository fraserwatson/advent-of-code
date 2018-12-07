input = open("/Users/fraser/Projects/advent-of-code/07/input.txt").read().splitlines()

characters = set()
needs_done = []
depends_on = []

instructions = ''

for line in input:
    first_step = line[5]
    next_step = line[36]
    characters.add(first_step)
    characters.add(next_step)
    needs_done.append(first_step)
    depends_on.append(next_step)

for i in range(len(characters)):
    test_letters = []
    step_letter = ''
    for character in characters:
        if character not in depends_on:
            test_letters.append(character)
    step_letter = sorted(test_letters)[0]
    instructions = instructions + step_letter
    characters.remove(step_letter)
    find_indices = [needs_done[x] == step_letter for x in range(len(needs_done))]
    indices = [i for i, x in enumerate(find_indices) if x]
    needs_done = [j for i, j in enumerate(needs_done) if i not in indices]
    depends_on = [j for i, j in enumerate(depends_on) if i not in indices]

print(instructions)


'''
for character in sorted(characters):
    f.write('{0} = BashOperator(task_id="{0}", bash_command="", dag=dag)\n'.format(character))

for line in input:
    first_step = line[5]
    next_step = line[36]
    f.write('{0}.set_downstream({1})\n'.format(first_step, next_step))

f.close()
'''
