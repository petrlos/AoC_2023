#Advent of Code 2023: Day 15
def get_hash(str):
    result = 0
    for char in str:
        result = ((result + ord(char)) * 17) % 256
    return result

#MAIN
with open("test.txt") as file:
    line = file.read().split(",")

print("Part 1:",sum([get_hash(group) for group in line]))