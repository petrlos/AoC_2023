#Advent of Code 2023: Day 2
import re

class Bag:
    def __init__(self, colours):
        self.red, self.green, self.blue = colours

    @property
    def bag_possible(self):
        return (self.red <= 12) and (self.green <= 13) and (self.blue <= 14)

    @property
    def power(self):
        return self.red * self.blue * self.green

def parsing(line):
    regexes = [re.compile(r"(\d+) red"), re.compile(r"(\d+) green"), re.compile(r"(\d+) blue")]
    colours = []
    for regex in regexes:
        max_count = max(list(map(int, regex.findall(line))))
        colours.append(max_count)
    return colours

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

bag_ids = []
powers = []
for game, line in enumerate(lines, start = 1):
    new_bag = Bag(parsing(line))
    if new_bag.bag_possible:
        bag_ids.append(game)
    powers.append(new_bag.power)

print("Part 1:",sum(bag_ids))
print("Part 2:",sum(powers))