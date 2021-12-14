import numpy as np

with open("input10.txt", "r") as f:
    lines = f.readlines()

prompt = [line.strip() for line in lines]


def flip(char):
    if char == ")":
        return "("
    elif char == "]":
        return "["
    elif char == "}":
        return "{"
    elif char == ">":
        return "<"


def filter_two_piece_chunks(prompt):
    clean_prompt = []
    for line in prompt:
        line = [char for char in line]
        for i, char in enumerate(line):
            try:
                if line[i] == flip(line[i + 1]):
                    line.pop(i + 1)
                    line.pop(i)
            except IndexError:
                pass
        line = "".join(line)
        clean_prompt.append(line)
    return clean_prompt


for _ in range(25):
    prompt = filter_two_piece_chunks(prompt)


def orientation(char):
    if char in "([{<":
        return "left"
    elif char in ")]}>":
        return "right"


# The first illegal character should be one of a two piece pair:
def filter_corrupt_line(line):
    line = [char for char in line]
    for i, char in enumerate(line):
        try:
            if orientation(line[i]) == "left" and orientation(line[i + 1]) == "right":
                if line[i] != flip(line[i + 1]):
                    return None
        except IndexError:
            return line


prompt = [line for line in prompt if filter_corrupt_line(line) is not None]


def score_completion_string(string):
    score = 0
    for char in string:
        score *= 5
        if char in "()":
            score += 1
        elif char in "[]":
            score += 2
        elif char in "{}":
            score += 3
        elif char in "<>":
            score += 4
    return score


scores = []
for line in prompt:
    scores.append(score_completion_string(line[::-1]))
scores = np.array(scores)
print(np.median(scores))
