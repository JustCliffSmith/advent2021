import numpy as np

# Puzzle 7
with open("input4.txt", "r") as f:
    lines = f.readlines()

# Get the list of moves from the first line.
moves = lines[0].rstrip().split(",")
moves = [int(move) for move in moves]
lines = lines[1:]
# Filter out blank lines, we will leverage that each board is five rows.
lines = [line for line in lines if line != "\n"]

print(moves)

boards = []
board = []
for i, line in enumerate(lines):
    if i % 5 == 0 or i == len(lines) - 1:
        if i == len(lines) - 1:
            clean_line = line.strip().split()
            board.append([int(value) for value in clean_line])
        board = np.array(board)
        boards.append(board)
        board = []
    clean_line = line.strip().split()
    board.append([int(value) for value in clean_line])
boards = boards[1:]  # The first board is null.


def check_winner(board, masked_boards):
    for i, (board, mask) in enumerate(zip(board, masked_boards)):
        masked_board = np.ma.masked_array(board, mask)
        if (5 in mask.sum(axis=0)) or (5 in mask.sum(axis=1)):
            board_total = np.ma.masked_array(boards[i], masked_boards[i]).sum()
            return i, board_total
    return None, None

  
masked_boards = [board == 123456789 for board in boards]
for move in moves:
    # Update masks.
    masked_boards_new = [board == move for board in boards]
    masked_boards = [old + new for old, new in zip(masked_boards, masked_boards_new)]
    winner_index, board_total = check_winner(boards, masked_boards)
    if winner_index is not None:
        print(move, board_total)
        print(move * board_total)
        break

# Puzzle 8

masked_boards = [board == 123456789 for board in boards]
while len(boards) > 0: # Oops this is super inefficient and maybe unPythonic...
    for move in moves:
        # Update masks.
        masked_boards_new = [board == move for board in boards]
        masked_boards = [
            old + new for old, new in zip(masked_boards, masked_boards_new)
        ]
        winner_index, board_total = check_winner(boards, masked_boards)
        if winner_index is not None:
            break
    del boards[winner_index]
    del masked_boards[winner_index]
print(move, board_total)
print(move * board_total)
