#Advent of Code 2023: Day 20
from collections import deque

class Module:
    def __init__(self, type, name, targets):
        self.name = name
        self.type = type
        self.targets = targets
        self.incoming = dict()
        self.status = False  # at the start are all off

    @property
    def all_high(self):
        for pulse in self.incoming.values():
            if pulse in ["low", None]:
                return False
        return True

    def __repr__(self):
        if self.type == "%":
            return f"{self.type}{self.name}: Targ: {self.targets}, Status:{self.status}"
        else:
            return f"{self.type}{self.name}: Targ: {self.targets}, Inp:{self.incoming}"

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

modules = dict()
broadcaster_targets = []
for line in lines:
    left, right = line.split(" -> ")
    targets = right.split(", ")
    if line.startswith("broadcaster"):
        broadcaster_targets = targets
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(type, name, targets)

for name, module in modules.items():
    for target in module.targets:
        if target in modules.keys():
            if modules[target].type == "&":
                modules[target].incoming[name] = None

queue = deque()
total_low = 0
total_high = 0
for _ in range(1000):
    total_low += 1
    for target in broadcaster_targets:
        total_low += 1 #broadcaster to target - always low
        if modules[target].status == True:
            modules[target].status = False
            queue.append((target, "low"))
        else:
            modules[target].status = True
            queue.append((target, "high"))
    while queue:
        sender, pulse = queue.popleft()
        for t in modules[sender].targets:
            if pulse == "high":
                total_high += 1
            else:
                total_low += 1
            if t not in modules.keys():
                continue
            if modules[t].type == "%":
                if pulse == "low":
                    if modules[t].status == True:
                        modules[t].status = False
                        queue.append((t, "low"))
                    else:
                        modules[t].status = True
                        queue.append((t, "high"))
            else:
                modules[t].incoming[sender] = pulse
                if modules[t].all_high:
                    queue.append((t, "low"))
                else:
                    queue.append((t, "high"))
print("Part 1:",total_high*total_low)