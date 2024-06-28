# Name: Felicity Cundiff
# CSE 160
# Spring 2024
# Checkin 7


# Problem 1
def first_character(input_list):
    '''
    Write a one-line list comprehension that returns a list containing
    the first letter of each string in the input list.
    Returns an empty list if the input list has no elements

    Arguments:
        input_list: a list of strings. You may assume all strings
        are at least one character long

    Returns: a list of strings
    '''
def first_character(input_list):
    return [s[0] for s in input_list]

assert first_character([]) == []
assert first_character(['a']) == ['a']
assert first_character(['cse160']) == ['c']
assert first_character(['one', 'two']) == ['o', 't']
assert first_character(['one', 'two', 'three', 'four', 'five']) == \
                       ['o', 't', 't', 'f', 'f']
assert first_character(['1']) == ['1']
assert first_character(['one', 'one', 'one']) == ['o', 'o', 'o']
assert first_character(['fourty-two', 'life', 'universe', 'everything']) == \
                       ['f', 'l', 'u', 'e']

# Problem 2
def larger_elements(input_list, input_num):
    '''
    Write a one line list comprehension that returns a list
    containing all the elements of a given list that
    are larger than a given number.
    Reutrn an empty set if input_list is empty

    Arguments:
        input_list: a list of integers
        input_num: an integer

    Returns: A list containing all the elements of the input_list higher
    than input_num

    '''
def larger_elements(input_list, input_num):
    return [x for x in input_list if x > input_num]

assert larger_elements([], 5) == []
assert larger_elements([5], 5) == []
assert larger_elements([6], 5) == [6]
assert larger_elements([4], 5) == []
assert larger_elements([1, 2, 3], 5) == []
assert larger_elements([5, 6, 7, 8], 5) == [6, 7, 8]
assert larger_elements([-1, 5, 134, -15, 2], 100) == [134]
assert larger_elements([-1, 64, 3, -20, 2], -5) == [-1, 64, 3, 2]
