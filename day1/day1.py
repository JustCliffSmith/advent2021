import os
from pathlib import Path

# Puzzle 1
path = Path(os.getcwd()) / "input1.txt"
with open(path, "r") as f:
    lines = f.readlines()

readings = [int(reading.rstrip()) for reading in lines]


def get_increase_count(readings):
    current_reading = readings[0]
    increase_count = 0
    for next_reading in readings[1:]:
        if next_reading > current_reading:
            increase_count += 1
        current_reading = next_reading

    print(increase_count)


get_increase_count(readings)

# Puzzle 2

windowed_readings = []
for i in range(len(readings)):
    try:
        windowed_readings.append(readings[i] + readings[i + 1] + readings[i + 2])
    except IndexError:
        break

get_increase_count(windowed_readings)
