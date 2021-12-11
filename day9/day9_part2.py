import numpy as np

with open("input9_test.txt", "r") as f:
    lines = f.readlines()

height_map = np.array([[int(height) for height in line.strip()] for line in lines])


def is_lowpoint(height_map, i, j):
    loc_point = height_map[i][j]
    if i - 1 >= 0 and i - 1 < height_map.shape[0]:
        up = height_map[i - 1][j]
    else:
        up = 9
    if i + 1 >= 0 and i + 1 < height_map.shape[0]:
        down = height_map[i + 1][j]
    else:
        down = 9
    if j + 1 >= 0 and j + 1 < height_map.shape[1]:
        left = height_map[i][j + 1]
    else:
        left = 9
    if j - 1 >= 0 and j - 1 < height_map.shape[1]:
        right = height_map[i][j - 1]
    else:
        right = 9
    if loc_point < up and loc_point < down and loc_point < left and loc_point < right:
        return True
    else:
        return False


def calculate_basin_size(height_map, i, j):
    """ Start from the low point, then go in each direction until a nine is hit"""
    basin_size = 1 # account for the low point
    moved_i = i
    moved_j = j
    print(moved_i, moved_j)
    value = 0
    while value < 9:
        moved_i += 1
        if moved_i>= 0 and moved_i < height_map.shape[0]:
            value = height_map[moved_i][moved_j]
            if value < 9:
                basin_size += 1
                print(moved_i, moved_j, value, basin_size)
        else:
            moved_i = i
            break
        #print(moved_i, moved_j, value, basin_size)
    value = 0
    while value < 9:
        moved_i -= 1
        if moved_i >= 0 and moved_i < height_map.shape[0]:
            value = height_map[moved_i][moved_j]
            if value < 9:
                basin_size += 1
                print(moved_i, moved_j, value, basin_size)
        else:
            moved_i = i
            break
        #print(moved_i, moved_j, value, basin_size)
    value = 0
    while value < 9:
        moved_j += 1
        if moved_j >= 0 and moved_j < height_map.shape[1]:
            value = height_map[moved_i][moved_j]
            if value < 9:
                basin_size += 1
                print(moved_i, moved_j, value, basin_size)
        else:
            moved_j = j
            break
        #print(moved_i, moved_j, value, basin_size)
    value = 0
    while value < 9:
        moved_j -= 1
        if moved_j >= 0 and moved_i < height_map.shape[1]:
            value = height_map[moved_i][moved_j]
            if value < 9:
                basin_size += 1
                print(moved_i, moved_j, value, basin_size)
        else:
            moved_j = j
            break
        #print(moved_i, moved_j, value, basin_size)
    return basin_size


low_point_map = np.ones(height_map.shape)
basin_sizes = []
for i in range(height_map.shape[0]):
    for j in range(height_map.shape[1]):
        if is_lowpoint(height_map, i, j) is True:
            low_point_map[i][j] = 0
            basin_sizes.append(calculate_basin_size(height_map, i, j))
            print(i, j, calculate_basin_size(height_map, i, j))

basin_sizes = sorted(basin_sizes, reverse=True)
print(basin_sizes)
print(basin_sizes[0:3])

print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
