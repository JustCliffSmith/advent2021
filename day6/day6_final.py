with open("input6.txt", "r") as f:
    lines = f.readlines()

# In this case there's only one line.
starting_state = lines[0].strip().split(",")
state = [int(x) for x in starting_state]
print("Initial state:", state)

# Change this for part 1 (80 days) or part 2 (256 days).
days = 256

counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for s in state:
    counter[s] += 1

print(counter)

for day in range(1, days + 1):
    starting_zero_count = counter[0]
    counter[0] = counter[1]
    counter[1] = counter[2]
    counter[2] = counter[3]
    counter[3] = counter[4]
    counter[4] = counter[5]
    counter[5] = counter[6]
    counter[6] = counter[7] + starting_zero_count
    counter[7] = counter[8]
    counter[8] = starting_zero_count

fish_count = 0
for k, v in counter.items():
    fish_count += v
print(counter)
print(fish_count)
