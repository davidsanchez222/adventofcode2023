import re

with open("input.txt", "r") as file:
    puzzle_input = file.read().splitlines()

s = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip().split("\n")



instruction_pattern = puzzle_input[0]
nodes = puzzle_input[2:]
sample = {}

for line in nodes:
    base_node = line.split(" = ")[0]
    leftright = line.split(" = ")[1]
    leftright = re.findall(r"\(([A-Z]{3}),\s([A-Z]{3})\)", leftright)
    left = leftright[0][0]
    right = leftright[0][1]
    sample[base_node] = (left, right)


combo = "AAA"
steps = 0
while True:
    if combo == "ZZZ":
        break
    instruction_direction = instruction_pattern[steps % len(instruction_pattern)]
    base_node = sample[combo]
    left = base_node[0]
    right = base_node[1]

    if instruction_direction == "L":
        combo = left
    else:
        combo = right

    steps += 1

print(steps)
