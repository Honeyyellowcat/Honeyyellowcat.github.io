# Name: ...
# CSE 160
# Autumn 2023
# Checkin 4


# Problem 1
def first_letter(filename):
    '''
    Given a file name, return a string containing the first letter of
    each line in the file

    Arguments:
        filename: a string representing a filename

    Returns: a string made up of the first letter of each line of the
    file in order
    '''
    # your solution code should start here


assert first_letter("numbers.txt") == "ottffs"
assert first_letter("animals.txt") == "cspgcdchrm"


# Problem 2
def num_lower_val(max_val, input_dict):
    '''
    Return the number of values in the dictionary that are lower than the
    given int
    All values in the dictionary will be integers

    Arguments:
        max_val: an integer
        input_dict: a dictionary with int values

    Returns: An integer representing the number of key-value pairs in the
    dictionary where the value is smaller than max_val
    '''
    # your solution code should start here


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
    '''
    Given a list of strings representing the names of ducks
    and a list of integers representing their age,
    construct a dictionary containing a mapping of the ducks names
    to its age

    Arguments:
        duck_names: A list of strings
        duck_age: A list of ints where the int at index i
            represents the age of the duck from
            duck_names at index i

    Returns: An dictionary that maps the name of the ducks to their ages

    '''
    # your solution code should start here


assert duck_dict(["Bri"], [5]) == {"Bri": 5}
assert duck_dict(["Bri", "Kim"], [5, 6]) == {"Bri": 5, "Kim": 6}
assert duck_dict(["A", "B", "C"], [5, 8, 1]) == {"A": 5, "B": 8, "C": 1}
assert duck_dict(["A", "B", "C"], [1, 1, 1]) == {"A": 1, "B": 1, "C": 1}
assert duck_dict(["A1", "A2", "A3"], [100, 15, 55]) == \
                 {"A1": 100, "A2": 15, "A3": 55}
