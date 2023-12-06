#Advent of Code 2023: Day 6
from datetime import datetime
time_start = datetime.now()
import re

def get_dist_over_time(max_time, record):
    distances = []
    for time in range(max_time+1):
        distance = (max_time-time)*time
        distances.append(distance)
    return list(filter(lambda x: x > record, distances))

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

max_times = list(map(int,(re.findall(r"\d+",lines[0]))))
records = list(map(int,(re.findall(r"\d+",lines[1]))))

#Part 1
total_length = 1
for max_time, record in zip(max_times, records):
    distances = get_dist_over_time(max_time, record)
    total_length *= len(distances)
print("Part 1:",total_length)

#Part 2
max_time = int(lines[0][6:].replace(" ",""))
record = int(lines[1][10:].replace(" ",""))
distances = get_dist_over_time(max_time, record) #brute force ftw
#runtime about 10seconds
print("Part 2:", len(distances))
print("Total runtime:", datetime.now()-time_start)