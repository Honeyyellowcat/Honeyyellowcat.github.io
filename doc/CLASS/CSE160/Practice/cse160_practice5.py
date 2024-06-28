# Name: Felicity Cundiff
# Date: 5/3/2024
# CSE 160, Winter 2024
# Assignment: Coding Practice #5

# Problem 1
def student_grades(student_gradebook, assignment_num):
    student_name = {}
    for name in student_gradebook.items():
        student_grades = student_gradebook[name]
        if (student_grades[assignment_num] >= 50):
            student_name = student_name | set([name])
    return student_name


assert student_grades({("Tweety", "Bird"): [90, 50, 39]}, 1) == \
                      {("Tweety", "Bird")}
assert student_grades({("Tweety", "Bird"): [90, 50, 39]}, 3) == set()
assert student_grades({("Tweety", "Bird"): [90, 50, 39]}, 2) == \
                      {("Tweety", "Bird")}
assert student_grades({("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 3) == \
                        {("Hector", "Bulldog")}
assert student_grades({("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 2) == \
                        {("Tweety", "Bird")}
assert student_grades({("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 1) == \
                        {("Tweety", "Bird"), ("Hector", "Bulldog")}
assert student_grades({("Sylvester", "Stallone"): [19, 76, 76],
                       ("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 1) == \
                        {("Tweety", "Bird"), ("Hector", "Bulldog")}
assert student_grades({("Sylvester", "Stallone"): [19, 76, 76],
                       ("Hector", "Bulldog"): [51, 30, 100],
                       ("Tweety", "Bird"): [90, 50, 39]}, 3) == \
                        {("Sylvester", "Stallone"), ("Hector", "Bulldog")}


# Problem 2
def mutability_exercise(input_set, input_list, input_dict):
    input_set.update(input_dict.keys())  
    input_dict.update((k, 160) for k in input_dict)  
    output_list = [x for x in input_list if x not in input_set] 
    return output_list


input_set_one = {1, 2, 3, 4, 5}
input_list_one = [1, 6, 0, 15]
input_dict_one = {21: 5, 3: 6, 15: 2}
output_list_one = mutability_exercise(input_set_one, input_list_one,
                                      input_dict_one)

assert input_set_one == {1, 2, 3, 4, 5, 21, 15}
assert input_list_one == [1, 6, 0, 15]
assert input_dict_one == {21: 160, 3: 160, 15: 160}
assert output_list_one == [6, 0]

input_set_two = {2, 4, 8, 16, 4000}
input_list_two = [-2, 4, -8, 3]
input_dict_two = {160: 160, 2: 3, 4000: 120}
output_list_two = mutability_exercise(input_set_two, input_list_two,
                                      input_dict_two)

assert input_set_two == {2, 4, 8, 16, 4000, 160}
assert input_list_two == [-2, 4, -8, 3]
assert input_dict_two == {160: 160, 2: 160, 4000: 160}
assert output_list_two == [-2, -8, 3]