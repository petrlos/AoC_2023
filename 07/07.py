#Advent of Code 2023: Day 7
from collections import Counter

def get_hand_type(line, part1 = True):
    card, value = line.split(" ")
    if part1:
        counter = sorted(Counter(card).values(), reverse=True)
        translate = dict(zip("TJQKA", "10,11,12,13,14".split(",")))
    else:
        counter = sorted(Counter(card).values(), reverse=True)
        translate = dict(zip("TJQKA", "10,1,12,13,14".split(","))) #new values of cards - "J"=1
        if "J" in card:
            j_count = card.count("J")
            counter = sorted(Counter(card.replace("J","")).values(), reverse=True) #count all cards except "J"
            if len(counter) > 0:
                counter[0] += j_count #the most common card would become "J" - best combination
            else:
                counter = [5] #all five were "J" - five of kind with "J"s
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

part1 = True
for i in range(1,3):
    cards = []
    for line in lines:
        card = get_hand_type(line, part1)
        cards.append(card)
    cards = sorted(cards)
    print("Part {0}: {1}".format(i,count_winnings(cards)))
    part1 = False