import numpy as np

with open("input9.txt", "r") as f:
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


low_point_map = np.ones(height_map.shape)
for i in range(height_map.shape[0]):
    for j in range(height_map.shape[1]):
        if is_lowpoint(height_map, i, j) is True:
            low_point_map[i][j] = 0

# for row in low_point_map:
#    print(row)

low_point_map_values = np.ma.masked_array(height_map + 1, low_point_map)
print(low_point_map_values.sum())
