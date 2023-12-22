#Advent of Code 2023: Day 19
import re
class Workflow:
    def __init__(self, conditions):
        self.conditions = conditions.split(",")

    def check_conditions(self, part):
        for condition in self.conditions:
            if ":" in condition: #only target
                rule, target = condition.split(":")
            else:
                target = condition
            if ">" in condition: #is larger
                variable = rule[0]
                number = int(rule.split(">")[1])
                if part[variable] > number: #correct - return targer
                    return target
            elif "<" in condition: #is lower
                variable = rule[0]
                number = int(rule.split("<")[1])
                if part[variable] < number: #corrent - return target
                    return target
            else:
                return target #no match found - return target

def parse_workflows(lines):
    regex = re.compile(r"(\w+)\{(.+)\}")
    workflows = dict()
    for workflow in lines.splitlines():
        match = re.match(regex, workflow)
        name, conditions = match.group(1), match.group(2)
        workflows[name] = Workflow(conditions)
    return workflows

def parse_part(line):
    part = {}
    group = line[1:-1].split(",")
    for var in group:
        key, value = var.split("=")
        part[key] = int(value)
    return part

def check_part(part):
    current = "in"
    while current not in ["A", "R"]: #check conditions until not accepted or rejected
        current = workflows[current].check_conditions(part)
    return current == "A"

#MAIN
with open("data.txt") as file:
    lines = file.read().split("\n\n")

#dictionary: key = name, value = class Workout
workflows = parse_workflows(lines[0])
parts = lines[1]

result = 0
for part_raw in parts.splitlines():
    part = parse_part(part_raw) #dictionary: key = variable, value = number
    if check_part(part):
        result += sum(part.values())

print("Part 1:", result)


