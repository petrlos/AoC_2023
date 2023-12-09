#Advent of Code 2023: Day 9

def extrapolate_values(line, part1=True):
    numbers = list(map(int,line.split(" ")))
    first_on_line = [numbers[0]]
    last_on_line = [numbers[-1]]
    while set(numbers) != {0}:
        differences = []
        for first, second in zip(numbers[:-1], numbers[1:]):
            difference = second - first
            differences.append(difference)
        last_on_line.append(differences[-1])
        first_on_line.append(differences[0])
        numbers = differences
    if part1:
        one_up_right = 0
        for last in reversed(last_on_line):
            one_up_right = one_up_right + last
        return one_up_right
    else:
        one_up_left = 0
        for first in reversed(first_on_line):
            one_up_left = first - one_up_left
        return one_up_left
#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

checksum = 0
for line in lines:
    checksum += extrapolate_values(line)
print("Part 1:",checksum)

checksum = 0
for line in lines:
    checksum += extrapolate_values(line, part1 = False)
print("Part 2:",checksum)
