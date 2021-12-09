with open("input8.txt", "r") as f:
    lines = f.readlines()

signal_patterns, output_values = [], []
for line in lines:
    split_line = line.split(" | ")
    signal_patterns.append(split_line[0].strip().split())
    output_values.append(split_line[1].strip().split())

# For each signal pattern we need to determine a mapping.
number2segment = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
segment2number = {v: k for k, v in number2segment.items()}


def digit_sort(digit):
    return "".join(sorted(digit))


def unscramble_value(value, inverse_map):
    unscrambled_value = [inverse_map[c] for c in value]
    return digit_sort("".join(unscrambled_value))


def get_bef(signals):
    """ The segments b,e, and f show up a unique number of times (6, 4, and 9)"""
    all_digits = "".join(signals)
    for char in set(all_digits):
        char_count = all_digits.count(char)
        if char_count == 6:
            b = char
        elif char_count == 4:
            e = char
        elif char_count == 9:
            f = char
    return set(b), set(e), set(f)


def get_a(signals):
    two_digit = [signal for signal in signals if len(signal) == 2]
    three_digit = [signal for signal in signals if len(signal) == 3]
    return set(three_digit[0]) - set(two_digit[0])


def get_c_candidates(signals):
    all_digits = "".join(signals)
    candidates = []
    for char in set(all_digits):
        char_count = all_digits.count(char)
        if char_count == 8:
            candidates.append(char)
    return set(candidates)


all_letters = set("abcdefg")
total_value = 0
for signals, values in zip(signal_patterns, output_values):
    display = {}

    b, e, f = get_bef(signals)
    display["b"] = b
    display["e"] = e
    display["f"] = f

    a = get_a(signals)
    display["a"] = a

    # c and a both show up 8 times, but I already know a.
    c_candidates = get_c_candidates(signals)
    c = c_candidates - set(a)
    display["c"] = c

    six_digits = [signal for signal in signals if len(signal) == 6]
    known_so_far = b.union(e).union(f).union(a).union(c)
    six_digits = ["".join(list(set(signal) - known_so_far)) for signal in six_digits]
    g = [set(signal) for signal in six_digits if len(signal) == 1][0]
    display["g"] = g

    known_so_far = b.union(e).union(f).union(a).union(c).union(g)
    display["d"] = all_letters - known_so_far

    # for k, v in display.items(): print(k, v)

    # Logic to get the proper numbers out.
    inverse_display_map = {list(v)[0]: k for k, v in display.items()}
    display_value = []
    for value in values:
        clean_value = unscramble_value(value, inverse_display_map)
        display_value.append(str(segment2number[clean_value]))
    total_value += int("".join(display_value))
print(total_value)
