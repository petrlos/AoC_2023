#Advent of Code 2023: Day 19
from icecream import ic
from copy import deepcopy
import re
from collections import deque

def cut_intervals(interval, condition):
    cut_variable, sign, border = condition
    start, end = interval[cut_variable]
    if sign == "<": # result = (condtition accepted, condition not accepted), -1 = no match
        if border <= start:
            result = (-1, (start, end))
        elif border > end:
            result = ((start, end), -1)
        else:
            result = ((start, border-1), (border, end))
    elif sign == ">":
        if border >= end:
            result = (-1, (start, end))
        elif border < start:
            result = ((start, end), -1)
        else:
            result = ((border+1, end), (start, border))
    accepted, not_accepted = result
    interval_accepted = deepcopy(interval)
    if accepted != -1:
        interval_accepted[cut_variable] = accepted
    else:
        interval_accepted = -1
    if not_accepted != -1:
        interval[cut_variable] = not_accepted
    else:
        interval = -1
    return interval_accepted, interval

def parse_workflows(lines):
    regex = re.compile(r"(\w+)\{(.+)\}")
    workflows = dict()
    for workflow in lines:
        match = re.match(regex, workflow)
        name, conditions = match.group(1), match.group(2)
        workflows[name] = conditions.split(",")
    return workflows

def check_condition(interval, condition):
    if ":" in condition: #intervals must be cut
        cond, target = condition.split(":")
        interval["path"].append(target)
        if ">" in cond:
            cut_variable, border = cond.split(">")
            accepted, not_accepted = cut_intervals(interval, [cut_variable, ">", int(border)])
        elif "<" in cond:
            cut_variable, border = cond.split("<")
            accepted, not_accepted = cut_intervals(interval, [cut_variable, "<", int(border)])
    else:
        if condition == "R": #all rejected
            accepted = not_accepted = -1
        elif condition == "A": #all accepted
            interval["path"].append("A")
            accepted = interval
            not_accepted = -1
        else: #only target
            interval["path"].append(condition)
            accepted = interval
            not_accepted = -1
    return accepted, not_accepted

#MAIN
with open("data.txt") as file:
    lines = file.read().split("\n\n")

workflows = parse_workflows(lines[0].splitlines())

interval = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000), "path": ["in"]}
queue = deque([interval])

intervals_accepted = []

while queue:
    current = queue.popleft()
    if current == -1:
        continue
    if current["path"][-1] == "R":
        continue
    new_target = current["path"][-1]
    for condition in workflows[new_target]:
        accepted, not_accepted = check_condition(current, condition)
        if accepted != -1:
            if accepted["path"][-1] == "A":
                intervals_accepted.append(accepted)
            else:
                queue.append(accepted)
        if not_accepted != -1:
            current = deepcopy(not_accepted)

result = 0
for interval in intervals_accepted:
    multiplier = 1
    for letter in "xmas":
        lower, upper = interval[letter]
        multiplier *= (upper - lower + 1)
    result += multiplier
print(result)