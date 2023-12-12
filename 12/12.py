#Advent of Code 2023: Day 12
from datetime import datetime
import re

time_start = datetime.now()

with open("data.txt") as file:
    lines = file.read().splitlines()

reg_num = re.compile(r"\d+")
reg_hash = re.compile(r"#+")

check_sum = []
for line in lines:
    check_sum_line = 0
    qm_count = line.count("?")
    hash_count = line.count("#")
    groups = [int(num) for num in reg_num.findall(line)] #length of groups on original line

    comb = 2 ** (qm_count) #each "?"  might be "." or "#" -> might be represented by binary number
    qm_positions = [index for index, char in enumerate(line) if char == "?"] #positions of "?"
    for i in range(comb): #generate all combinations of positions
        new_line = list(line.split(" ")[0]) #take only first half of the line, transfer to list - easier to work with
        possible_hashes = bin(i)[2:].zfill(qm_count) #generate binary number in total length of "?".count
        if possible_hashes.count("1") + hash_count == sum(groups): #count of "1" in bin + hashes == total count
            for qm_position, possible_hash in zip(qm_positions, possible_hashes): #replace "?" with "#" or "."
                if int(possible_hash):
                    new_line[qm_position] = "#"
                else:
                    new_line[qm_position] = "."
            new_line = "".join(new_line)
            checker = [len(length) for length in reg_hash.findall(new_line)] #return lengths of all "#" groups
            if checker == groups:
                check_sum_line += 1
    check_sum.append(check_sum_line)
print("Part 1:", sum(check_sum))
print("Runtime: ", datetime.now() - time_start)