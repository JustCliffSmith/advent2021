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
                    # print("pop", line[i], line[i+1])
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
def find_wrong_two_piece_chunk(line):
    line = [char for char in line]
    for i, char in enumerate(line):
        try:
            if orientation(line[i]) == "left" and orientation(line[i + 1]) == "right":
                if line[i] != flip(line[i + 1]):
                    # print(line[i], line[i+1])
                    return line[i + 1]
        except IndexError:
            return None


def char_score(char):
    if char in "()":
        return 3
    elif char in "[]":
        return 57
    elif char in "{}":
        return 1197
    elif char in "<>":
        return 25137


first_error_score = 0
for line in prompt:
    wrong_char = find_wrong_two_piece_chunk(line)
    if wrong_char is not None:
        first_error_score += char_score(wrong_char)

print(first_error_score)
