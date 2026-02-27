# Name: Brendan
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

"""def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total


# Test cases
print("sum_all of [4, 3, 6] is:", sum_all([4, 3, 6]))
print("sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4]))"""

# I'll come back to this later
"""def cumulative_sum(number_list):
    total = 0
    res = []
    for num in number_list:
        total += num
        res.append(total)
    return res


print("cumulative sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6]))
print("cumulative sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4]))"""


# **********  Exercise 2.8 **********

def report_card():
    num_classes = int(input("Enter number of classes: "))
    class_name_list = []
    class_grade_list = []
    total_gpa = float(0)

    for i in range(num_classes):
        class_name_list.append(str(input("Enter class name: ")))
        class_grade_list.append(int(input("Enter class grade: ")))

    for i in range(num_classes):
        print(class_name_list[i], class_grade_list[i])

    for i in range(num_classes):
        total_gpa = total_gpa + class_grade_list[i]


    return f"Overall GPA {total_gpa / num_classes}"

# Test Cases
print(report_card())


# **********  Exercise 2.9 **********

# Write any helper functions you need here.

"""VOWELS = ['a', 'e', 'i', 'o', 'u']


def pig_latin(word):
    # word is a string to convert to pig-latin

    ##### YOUR CODE HERE #####
    return "Not Implemented Yet"
"""
# Test Cases
##### YOUR CODE HERE #####


# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here