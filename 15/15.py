#Advent of Code 2023: Day 15
def get_hash(str):
    result = 0
    for char in str:
        result = ((result + ord(char)) * 17) % 256
    return result

#MAIN
with open("data.txt") as file:
    line = file.read().split(",")

print("Part 1:",sum([get_hash(group) for group in line]))

hashmap = [[] for _ in range(256)]
lenses = {}
for item in line:
    if "=" in item: #put lens in box
        name, lens = item.split("=")
        hash = get_hash(name)
        if name not in hashmap[hash]:
            hashmap[hash].append(name)
        lenses[name] = int(lens) #save lens length
    elif "-" in item: #remove lens from box
        hash = get_hash(item[:-1])
        if item[:-1] in hashmap[hash]:
            hashmap[hash].remove(item[:-1])

result = 0
for box_id, box in enumerate(hashmap, start=1):
    for slot, item in enumerate(box, start=1):
        result += box_id*slot*lenses[item]
print("Part 2:", result)
