#Advent of Code 2023: Day 4
import re

with open("data.txt") as file:
    lines = file.read().splitlines()


score = []
counts = []
for cardid, line in enumerate(lines):
    card, winning_numbers = line.split(": ")[1].split("|")
    card_num = list(map(int,(re.findall(r"\d+",card))))
    winn_num = list(map(int,(re.findall(r"\d+",winning_numbers))))
    counter = 0
    for numb in card_num:
        if numb in winn_num:
            counter += 1
    if counter > 0:
        score.append(2 ** (counter - 1))
        counts.append(counter)
    else:
        score.append(0)
        counts.append(counter)
print(score)
print(counts)
print(sum(score))

part2 = [1]*len(counts)
for cardid, count in enumerate(counts):
    for i in range(count):
        part2[cardid+i+1] += part2[cardid]
print(sum(part2))

