# Name: Felicity Cundiff
# Date: 4/12/2024
# CSE 160, Winter 2024
# Assignment: Activity 4 - Coding Practice #4

# Problem 1
def first_letter(filename):
    with open(filename, 'r') as file:
        first_letters = [line[0] for line in file]
    return ''.join(first_letters)

assert first_letter("numbers.txt") == "ottffs"
assert first_letter("animals.txt") == "cspgcdchrm"

# Problem 2
def num_lower_val(max_val, input_dict):
    count = sum(1 for value in input_dict.values() if value < max_val)
    return count

assert num_lower_val(5, {"one": 1, "two": 2, "three": 3}) == 3
assert num_lower_val(-5, {"one": 1, "two": 2, "three": 3}) == 0
assert num_lower_val(5, {"five": 5, "two": 2, "three": 3}) == 2
assert num_lower_val(21, {"panda": 20}) == 1
assert num_lower_val(18, {"panda": 20}) == 0
assert num_lower_val(2, {10: 1, 11: 1, 5: 1, 99: 1}) == 4
assert num_lower_val(6, {10: 7, 6: 25, 3: 1, 2: 2, 3: 1}) == 2
assert num_lower_val(1000, {1: 1001, 2: 999, 3: 1002}) == 1

# Problem 3
def duck_dict(duck_names, duck_ages):
    duck_dict = dict(zip(duck_names, duck_ages))
    return duck_dict

assert duck_dict(["Bri"], [5]) == {"Bri": 5}
assert duck_dict(["Bri", "Kim"], [5, 6]) == {"Bri": 5, "Kim": 6}
assert duck_dict(["A", "B", "C"], [5, 8, 1]) == {"A": 5, "B": 8, "C": 1}
assert duck_dict(["A", "B", "C"], [1, 1, 1]) == {"A": 1, "B": 1, "C": 1}
assert duck_dict(["A1", "A2", "A3"], [100, 15, 55]) == {"A1": 100, "A2": 15, "A3": 55}
