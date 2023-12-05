#Advent of Code 2023: Day 5
import re
from datetime import datetime
time_start = datetime.now()

class Convertor:
    def __init__(self, lines):
        self.convert = [] #list of lists - start, end, delta
        for line in lines.split("\n")[1:]:
            new, start, steps = list(map(int,(re.findall(r"\d+",line))))
            self.convert.append([start, start+steps-1, new-start])

    def convert_numbers(self, numbers):
        result = []
        for number in numbers:
            found = False
            for convert in self.convert:
                if number >= convert[0] and number <= convert[1]:
                    found = True
                    result.append(number + convert[2])
            if not found: #number not found in any interval - return number
                result.append(number)
        return result

#MAIN
with open("data.txt") as file:
    lines = file.read().split("\n\n")

numbers = list(map(int,(re.findall(r"\d+",lines[0]))))

for line in lines[1:]:
    convertor = Convertor(line)
    numbers = convertor.convert_numbers(numbers)

print("Part 1:", min(numbers))
print("Runtime:", datetime.now() - time_start)