# Name: Felicity Cundiff
# Date: 4/12/2024
# CSE 160, Winter 2024
# Assignment: Activity 3 - Coding Practice #3

# Problem 1
# your solution code should start here
def letter_count(string, letter):
    return string.count(letter)

# Problem 2
def letter_multiply(num, letter):
    if num < 0:
        return "invalid value for num"
    else:
        return letter * num

# Problem 3
# your solution code should start here
def glitchy_message(msg):
    result = ""
    for char in msg:
        count = letter_count(msg, char)
        result += letter_multiply(count, char)
    return result

print(letter_count("hi", 'h'))  # returns 1
print(letter_count("festival", 'q'))  # returns 0
print(letter_count("astronomy", 'o'))  # returns 2

print(letter_multiply(7, 'b'))  # returns "bbbbbbb"
print(letter_multiply(2, '&'))  # returns "&&"
print(letter_multiply(0, 'a'))  # returns ""

print(glitchy_message("letter"))  # returns "leetttteer"
print(glitchy_message("banana"))  # returns "baaannaaannaaa"
print(glitchy_message("paint"))  # returns "paint"