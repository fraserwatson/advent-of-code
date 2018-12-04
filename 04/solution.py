from datetime import datetime

text_file = open("/Users/fraser/Projects/advent-of-code/04/input.txt", "r")
input = text_file.readlines()

datetime_objects = []
for item in input:
    item_datetime = item[1:17]
    datetime_objects.append(datetime.strptime(item_datetime, '%Y-%m-%d %H:%M'))

new_input = [x for _,x in sorted(zip(datetime_objects, input))]

guard_sleep_times = {}

for line in new_input:
    # Determine the type of line
    if line[19] == 'G': # new guard id
        id = line[26:30]
        if id not in guard_sleep_times:
            guard_sleep_times[id] = [0] * 60
    if line[19] == 'f': # guard fell asleep
        sleep_start_time = int(line[15:17])
    if line[19] == 'w': # guard wakes up
        sleep_times = [0] * 60
        sleep_end_time = int(line[15:17])
        for i in range(sleep_start_time, sleep_end_time):
            sleep_times[i] = 1
        guard_sleep_times[id] = [sum(x) for x in zip(sleep_times, guard_sleep_times[id])]

max_mins_asleep = 0
id_max_mins_asleep = ''

for id in guard_sleep_times:
    mins_asleep = sum(guard_sleep_times[id])
    if mins_asleep > max_mins_asleep:
        max_mins_asleep = mins_asleep
        id_max_mins_asleep = id

print(max_mins_asleep)
print(id_max_mins_asleep)
print(guard_sleep_times[id_max_mins_asleep].index(max(guard_sleep_times[id_max_mins_asleep])))

most_slept_minute = 0
most_times_in_one_minute = 0
id_most_slept_minute = ''

for id in guard_sleep_times:
    guard_most_times_in_one_minute = max(guard_sleep_times[id])
    if guard_most_times_in_one_minute > most_times_in_one_minute:
        most_times_in_one_minute = guard_most_times_in_one_minute
        most_slept_minute = guard_sleep_times[id].index(max(guard_sleep_times[id]))
        id_most_slept_minute = id

print(most_slept_minute)
print(most_times_in_one_minute)
print(id_most_slept_minute)
