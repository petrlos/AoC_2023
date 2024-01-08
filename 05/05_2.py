#Advent of Code 2023: Day 5:
def convert_number_up(x, ranges):
    for interval in ranges:
        dest, source, length = interval
        if x in range(dest, dest+length):
            return x + (source - dest)
    return x

with open("data.txt") as file:
    lines = file.read().split("\n\n")

seeds_str, *convertors_str = lines

seeds = [] #generate intervals=ranges of seeds
seeds_str = seeds_str.split(" ")[1:]
for index in range(len(seeds_str)// 2):
    start, end = int(seeds_str[2*index]), int(seeds_str[2*index+1])
    seeds.append(range(start, start+end))

convertors = [] #generate intervals of converting maps
for convertor in convertors_str:
    ranges = []
    for line in convertor.split("\n")[1:]:
        dest, source, length = list(map(int, line.split(" ")))
        ranges.append([dest, source, length])
    convertors.append(ranges)

results = []
#tested all numbers from 20m to 50m, total runtime about 15 mins
#50.600.000 is really close to MY result, so that runtime is mimimal
x = 50600000
while not results:
    x += 1 #test every number
    start = x
    for convertor in reversed(convertors): #get corresponding seed number from location number
        start = convert_number_up(start, convertor)
    for seed in seeds: #if in interval, save to result, break while
        if start in seed:
            results.append(x)
print("Part 2:", results[0])