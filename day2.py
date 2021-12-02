# Puzzle 3
with open("input2.txt", "r") as f:
    lines = f.readlines()

# lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8","forward 2"]
directions = [direction.rstrip() for direction in lines]

horizontal = 0
depth = 0
for direction in directions:
    split_direction = direction.split(" ")
    direction = split_direction[0]
    amount = int(split_direction[1])
    if direction == "forward":
        horizontal += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount

print(f"Horiztonal: {horizontal:,}")
print(f"Depth: {depth:,}")
print(f"Multiplied: {horizontal * depth:,}")

# Puzzle 4

horizontal, depth, aim = 0, 0, 0
for direction in directions:
    split_direction = direction.split(" ")
    direction = split_direction[0]
    amount = int(split_direction[1])
    if direction == "forward":
        horizontal += amount
        depth += (aim * amount)
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount

print(f"Horiztonal: {horizontal:,}")
print(f"Depth: {depth:,}")
print(f"Aim: {aim:,}")
print(f"Multiplied: {horizontal * depth}")
