import numpy as np

with open("input7.txt", "r") as f:
    lines = f.readlines()

# In this case there's only one line.
horiz_pos = lines[0].strip().split(",")
horiz_pos = [int(x) for x in horiz_pos]

minimum_pos = np.array(horiz_pos).min()
maximum_pos = np.array(horiz_pos).max()

print(minimum_pos, maximum_pos)


def calculate_fuel_cost(distance):
    move_cost = 0
    for i in range(1, distance + 1):
        move_cost += 1 * i
    return move_cost


fuel_cost_all = []
for pos in range(minimum_pos, maximum_pos):
    fuel_cost = 0
    for crab_pos in horiz_pos:
        distance = abs(crab_pos - pos)
        fuel_cost += calculate_fuel_cost(distance)
    fuel_cost_all.append(fuel_cost)
    # print(f"Cost to move all crabs to pos {pos}: {fuel_cost}")
fuel_cost_all = np.array(fuel_cost_all)
cheapest_pos = np.argmin(fuel_cost_all)
print(f"Cheapest position: {cheapest_pos} with cost {fuel_cost_all[cheapest_pos]}")
