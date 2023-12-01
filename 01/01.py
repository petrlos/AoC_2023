#Advent of Code 2023 - Day 1
import re

def get_first_last_number(line): #find all ciphers in line, return first and last
    numbers = list(map(str, re.findall(r"\d", line)))
    number = int(numbers[0] + numbers[-1])
    return number

def find_numbers(line, numbers_str):
    positions = []
    for number, str_number in enumerate(numbers_str, start=1):
        indexes = [ind.start() for ind in re.finditer(str_number, line)]
        for index in indexes:
            if index >= 0:
                positions.append([index,str(number)])
    return positions

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

#PART 1
check_sum = 0
for line in lines:
    check_sum += get_first_last_number(line)
print("Part 1:", check_sum)

#PART2
check_sum = 0
for line in lines:
    number_words = "one, two, three, four, five, six, seven, eight, nine".split(", ")
    number_ciphers = "123456789"
    numbers_found = []
    numbers_found += find_numbers(line, number_words) #find indexes of all "word numbers"
    numbers_found += find_numbers(line, number_ciphers) #find indexes of all "ciphers"
    numbers_found.sort() #sort list
    result = int(numbers_found[0][1] + numbers_found[-1][1]) #get first and last number
    check_sum += result

print("Part 2:",check_sum)

