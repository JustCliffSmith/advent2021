import numpy as np

# Puzzle 4
with open("input3.txt", "r") as f:
    lines = f.readlines()

diagnostics = [diagnostic.rstrip() for diagnostic in lines]


def get_median_bit(diagnostics, i):
    """Get the median bit for a column i of data."""
    column = np.array([])
    for diagnostic in diagnostics:
        column = np.append(column, int(diagnostic[i]))
    median = np.median(column)
    # Don't break ties according to the rules because of the digit flip later.
    if median == 0.5:
        median = 1.0
    return median


digits_count = len(diagnostics[0])
median_digit = []
# Iterate over columns and get the median bit (technically should be mode).
for i in range(digits_count):
    median_bit = get_median_bit(diagnostics, i)
    median_digit.append(median_bit)

median_number = "".join([str(int(digit)) for digit in median_digit])
print("Gamma rate", median_number, int(median_number, 2))

# Get the complement of each bit.
inverse_median = []
for number in median_number:
    if number == "0":
        inverse_median.append(1)
    else:
        inverse_median.append(0)

inverse_median = "".join([str(number) for number in inverse_median])
print("Epsilon rate", inverse_median, int(inverse_median, 2))

print("Power: ", int(median_number, 2) * int(inverse_median, 2))

# Puzzle 5

ox_rating = []
# Same as before, but now need to filter for only the dignostics that have the correct
# beginning. When a single one remains use that as the ox_rating.
for i in range(digits_count):
    if i == 0:
        median_bit = get_median_bit(diagnostics, i)
        ox_rating.append(median_bit)
    else:
        ox_rating_sofar = "".join([str(int(num)) for num in ox_rating])
        diagnostics_filtered = [d for d in diagnostics if d.startswith(ox_rating_sofar)]
        if len(diagnostics_filtered) == 1:
            ox_rating = diagnostics_filtered
            break
        median_bit = get_median_bit(diagnostics_filtered, i)
        ox_rating.append(median_bit)

ox_rating = "".join([str(int(num)) for num in ox_rating])
print("Ox rating:", ox_rating, int(ox_rating, 2))


def flip_digit(digit):
    if int(digit) == 1:
        return 0
    else:
        return 1


co_rating = []
for i in range(digits_count):
    if i == 0:
        median_bit = get_median_bit(diagnostics, i, co2=True)
        median_bit = flip_digit(median_bit)
        co_rating.append(median_bit)
    else:
        co_rating_sofar = "".join([str(int(num)) for num in co_rating])
        diagnostics_filtered = [d for d in diagnostics if d.startswith(co_rating_sofar)]
        if len(diagnostics_filtered) == 1:
            co_rating = diagnostics_filtered
            break
        median_bit = get_median_bit(diagnostics_filtered, i, co2=True)
        median_bit = flip_digit(median_bit)
        co_rating.append(median_bit)

co_rating = "".join([str(int(num)) for num in co_rating])
print("CO2 rating:", co_rating, int(co_rating, 2))

print("Life support:", int(ox_rating, 2) * int(co_rating, 2))
