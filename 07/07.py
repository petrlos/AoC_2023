#Advent of Code 2023: Day 7
from collections import Counter

def get_hand_type(line):
    card, value = line.split(" ")
    counter = sorted(Counter(card).values(),reverse=True)
    translate = dict(zip("TJQKA", "10,11,12,13,14".split(",")))
    new_hand_name = []
    if counter == [1,1,1,1,1]:
        hand_type = 0
    elif counter == [2,1,1,1]:
        hand_type = 1
    elif counter == [2,2,1]:
        hand_type = 2
    elif counter == [3,1,1]:
        hand_type = 3
    elif counter == [3,2]:
        hand_type = 4
    elif counter == [4,1]:
        hand_type = 5
    elif counter == [5]:
        hand_type = 6
    else:
        hand_type = -1
    for char in card:
        if char in translate.keys():
            new_hand_name.append(int(translate[char]))
        else:
            new_hand_name.append(int(char))
    return [hand_type, new_hand_name, int(value)]

def count_winnings(cards):
    result = 0
    for index, card in enumerate(cards, start=1):
        result += index * card[2]
    return result

#MAIN

with open("data.txt") as file:
    lines = file.read().splitlines()

cards = []
for line in lines:
    card = get_hand_type(line)
    cards.append(card)

#Part 1
cards = sorted(cards)
print("Part 1:",count_winnings(cards))