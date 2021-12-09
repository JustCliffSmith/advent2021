import numpy as np

with open("input8.txt", "r") as f:
    lines = f.readlines()

signal_patterns, output_values = [], []
for line in lines:
    split_line = line.split(" | ")
    signal_patterns.append(split_line[0].strip().split())
    output_values.append(split_line[1].strip().split())

print(signal_patterns)
print(output_values)

count = 0
for values in output_values:
    for value in values:
        if len(value) in [2, 3, 4, 7]:
            count += 1

print(count)
