import numpy as np

with open("input6_test.txt", "r") as f:
    lines = f.readlines()

# In this case there's only one line.
starting_state = lines[0].strip().split(",")
state = [int(x) for x in starting_state]
print("Initial state:", state)

# Change this for day 1 (80 days) or day 2 (256 days).
days = 256

def zero_count(state):
    zero_count = 0
    for item in state:
        if item ==0:
            zero_count += 1
    return zero_count

for day in range(1, days+1):
    state = [*state, *([9] * zero_count(state))]
    #state = [item -1 for item in state]
    #state = [6 if item == -1 else item for item in state]
    state = [6 if item == 0 else item -1 for item in state]
    if day %  16 == 0:
        print(f"After {day} days:", len(state))
