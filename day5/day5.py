import numpy as np

# Puzzle 9
with open("input5.txt", "r") as f:
    lines = f.readlines()

# Parse the lines into a list of tuple pairs.
raw_coords = [line.strip().split(" -> ") for line in lines]

coord_pairs = []
for coord in raw_coords:
    first_pair = coord[0].split(",")
    first_pair = [int(c) for c in first_pair]
    second_pair = coord[1].split(",")
    second_pair = [int(c) for c in second_pair]
    new_coord = [first_pair, second_pair]
    coord_pairs.append(new_coord)

# Get the biggest x and y coords so we can make the grid.
biggest_x, biggest_y = 0, 0
for coord_pair in coord_pairs:
    x1, x2 = coord_pair[0][0], coord_pair[1][0]
    y1, y2 = coord_pair[0][1], coord_pair[1][1]
    if x1 > biggest_x:
        biggest_x = x1
    elif x2 > biggest_x:
        biggest_x = x2
    if y1 > biggest_y:
        biggest_y = y1
    elif y2 > biggest_y:
        biggest_y = y2
board = [[0] * (biggest_x + 1) for _ in range(biggest_y + 1)]


def mark_board(board, x, y):
    mark = board[y][x]
    board[y][x] = int(mark) + 1
    return board


def sort_pair(i, j):
    if i > j:
        return j, i
    else:
        return i, j


for coord_pair in coord_pairs:
    x1, x2 = coord_pair[0][0], coord_pair[1][0]
    y1, y2 = coord_pair[0][1], coord_pair[1][1]
    if x1 == x2:
        y1, y2 = sort_pair(y1, y2)
        for y in range(y1, y2 + 1):
            board = mark_board(board, x1, y)
    elif y1 == y2:
        x1, x2 = sort_pair(x1, x2)
        for x in range(x1, x2 + 1):
            board = mark_board(board, x, y1)

print(np.sum(np.array(board) > 1))

# Puzzle 10

board = [[0] * (biggest_x + 1) for _ in range(biggest_y + 1)]
for coord_pair in coord_pairs:
    x1, x2 = coord_pair[0][0], coord_pair[1][0]
    y1, y2 = coord_pair[0][1], coord_pair[1][1]
    if x1 == x2:
        y1, y2 = sort_pair(y1, y2)
        for y in range(y1, y2 + 1):
            board = mark_board(board, x1, y)
    elif y1 == y2:
        x1, x2 = sort_pair(x1, x2)
        for x in range(x1, x2 + 1):
            board = mark_board(board, x, y1)
    elif x2 >= x1:  # left to right
        if y2 >= y1:  # up to down
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                board = mark_board(board, x, y)
        else:  # down to up
            for x, y in zip(range(x1, x2 + 1), list(range(y2, y1 + 1))[::-1]):
                board = mark_board(board, x, y)
    elif x1 > x2:  # right to left
        if y1 > y2:  # down to up
            for x, y in zip(list(range(x2, x1 + 1)), list(range(y2, y1 + 1))):
                board = mark_board(board, x, y)
        else:  # up to down
            for x, y in zip(list(range(x2, x1 + 1))[::-1], range(y1, y2 + 1)):
                board = mark_board(board, x, y)

print(np.sum(np.array(board) > 1))
