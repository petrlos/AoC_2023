#Advent of Code 2023: Day 2
class Bag:
    def __init__(self):
        self.red = []
        self.green = []
        self.blue = []
        self.red_max = 0
        self.green_max = 0
        self.blue_max = 0
        self.power = 0

    def get_max(self):
        self.red_max = max(self.red)
        self.green_max = max(self.green)
        self.blue_max = max(self.blue)

    def bag_possible(self):
        if self.red_max > 12:
            return False
        elif self.green_max > 13:
            return False
        elif self.blue_max > 14:
            return False
        return True

    def sum_up(self):
        self.power = self.red_max * self.blue_max * self.green_max

def get_cubes_per_game(line):
    current_bag = Bag()
    line = line.split(": ")[1]
    turns = line.split("; ")
    for turn in turns:
        cubes = turn.split(", ")
        for cube in cubes:
            count, colour = cube.split(" ")
            if colour == "blue":
                current_bag.blue.append(int(count))
            elif colour == "red":
                current_bag.red.append(int(count))
            elif colour == "green":
                current_bag.green.append(int(count))
    current_bag.get_max()
    current_bag.sum_up()
    return current_bag

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

bags = []
powers = []
for game, line in enumerate(lines, start = 1):
    new_bag = get_cubes_per_game(line)
    if new_bag.bag_possible():
        bags.append(game)
    powers.append(new_bag.power)

print("Part 1:",sum(bags))
print("Part 2:",sum(powers))