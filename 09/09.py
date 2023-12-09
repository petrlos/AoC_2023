#Advent of Code 2023: Day 9

def extrapolate_values(line):
    numbers = list(map(int,line.split(" ")))
    last_on_line = [numbers[-1]]
    while set(numbers) != {0}:
        differences = []
        for first, second in zip(numbers[:-1], numbers[1:]):
            difference = second - first
            differences.append(difference)
        last_on_line.append(differences[-1])
        numbers = differences
    one_up = 0
    for last in reversed(last_on_line):
        one_up = one_up + last
    return one_up

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

checksum = 0
for line in lines:
    checksum += extrapolate_values(line)

print(checksum)