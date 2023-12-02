#Advent of Code 2023: Day 2
class Bag:
    def __init__(self):
        self.red = []
        self.green = []
        self.blue = []

    @property
    def bag_possible(self):
        return (self.red_max <= 12) and (self.green_max <= 13) and (self.blue_max <= 14)

    @property
    def red_max(self):
        return max(self.red)

    @property
    def green_max(self):
        return max(self.green)

    @property
    def blue_max(self):
        return max(self.blue)

    @property
    def power(self):
        return self.red_max * self.blue_max * self.green_max

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
    return current_bag

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

bag_ids = []
powers = []
for game, line in enumerate(lines, start = 1):
    new_bag = get_cubes_per_game(line)
    if new_bag.bag_possible:
        bag_ids.append(game)
    powers.append(new_bag.power)

print("Part 1:",sum(bag_ids))
print("Part 2:",sum(powers))