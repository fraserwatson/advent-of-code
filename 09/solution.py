input = open('/Users/fraser/Projects/advent-of-code/09/input.txt').read().split()

number_of_players = int(input[0])
last_marble = int(input[6])

from collections import deque

circle = deque([0])
players = [x for x in range(1, number_of_players + 1)]
scores = []
for _ in players:
    scores.append(0)


for marble in range(1, last_marble + 1):
    current_player = players.pop(0)
    players.append(current_player)
    if marble % 23 == 0:
        circle.rotate(7)
        scores[current_player-1] += circle.pop() + marble
        circle.rotate(-1)

    else:
        circle.rotate(-1)
        circle.append(marble)

print(max(scores))
