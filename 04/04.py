#Advent of Code 2023: Day 4
import re

def count_score(cards_count):
    cards_count = filter(lambda x: x > 0, cards_count) #dont need cards with zero score
    score = [2 ** (count - 1) for count in cards_count]
    return sum(score)

def part_2(matches):
    part2 = [1] * len(matches) #at the beginning each card once
    for cardid, count in enumerate(matches):
        for i in range(count):
            part2[cardid + i + 1] += part2[cardid]
    return sum(part2)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

matches = []
for line in lines:
    card_nums, winn_nums = line.split(": ")[1].split("|") #remove cardid + split cardnums from winni
    card_num = list(map(int,(re.findall(r"\d+",card_nums))))
    winn_num = list(map(int,(re.findall(r"\d+",winn_nums))))
    match = len(set(card_num) & set(winn_num)) # no order needed, only count
    if match > 0:
        matches.append(match)
    else:
        matches.append(0) #zero points cards needed for part2

print("Part 1:",count_score(matches))

print("Part 2:", part_2(matches))