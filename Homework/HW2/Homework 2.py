# Name: Brendan Lautissier
# Section:
# hw2.py
import random
import math
import cmath


##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 **********

"""def f1(x):
    print (x + 1)

def f2(x):
    return x + 1"""

# **********  Exercise 2.1 **********

# Rock, Paper, Scissors, but as a Function
"""def rps(user_choice):
    options = ["rock", "paper", "scissors"]
#    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in options:
        return "You are Error!"

    computer_choice = random.choice(options)
    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    if user_choice == computer_choice:
        return "Draw"
    elif  (user_choice == "rock"        and computer_choice == "scissors")  or \
          (user_choice == "paper"       and computer_choice == "rock")      or \
          (user_choice == "scissors"    and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"""
# Test Function Rock, Paper, Scissors
# print (rps("rock"))
# print (rps("paper"))
# print (rps("scissors"))

# ********** Exercise 2.2 **********

# Function "is_divisible" tests if "m" is divisible by "n"
"""def is_divisible(m, n):
    if m % n == 0:
        return True
    else:
        return False"""
# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print (is_divisible(10, 5))  # This should return True
#print (is_divisible(18, 7))  # This should return False
#print (is_divisible(42, 0))  # What should this return?
    # "ZeroDivisionError: interger modulo by zero" (Can't divide by zero)


# Can't use "!=", so then "==" return False, "!=" return True
"""def not_equal(a, b):
    if a == b:
        return False
    else:
        return True"""

# Test cases for not_equal
# print(not_equal("rock", "rock"))      # Suppose to return False   ( == ISN'T != )
# print(not_equal("rock", "scissors"))  # Suppose to return True    ( != IS != )

# ********** Exercise 2.3 **********

## 1 - multadd function
"""radians = (90.0 / 360.0) * 2 * math.pi
print(math.sin(radians))
print (math.cos(radians))"""

## 2 - Equations
##### YOUR CODE HERE #####
"""def multadd(a, b, c):
    return a * b + c"""

# Test Cases
#angle_test = (math.sin(math.pi/4) + math.cos(math.pi/4)/2)
"""angle_test = multadd(0.5, math.sin(math.pi/4), math.cos(math.pi/4))
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

#ceiling_test = math.ceil(276/19) + 2 * math.log(12, 7)
ceiling_test =  multadd(math.log(12, 7), 2, math.ceil(276/19))
print ("ceiling(276/19) + 2 log_7(12) is:")
print (ceiling_test)"""

## 3 - yikes function
"""def yikes(n):
    return multadd(n, math.pow(math.e,-n), math.sqrt(1 - math.pow(math.e,-n)))
print(yikes(5))"""

# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
"""def rand_divis_3():
   random_int = random.randint(0, 100)
   print(random_int)
   is_divisible_by_3 = random_int % 3 == 0
   return is_divisible_by_3
print(rand_divis_3())"""

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
#First number is the number of sides the die has, and the second is the number of dice rolled
"""def roll_dice(a, b):
    for b in range(b):
        dice_roll = random.randint(1, a)
        print(dice_roll)
    return "That's all folks!"

# Test Cases
print(roll_dice(6, 3))"""

# ********** Exercise 2.5 **********

# code for roots function
def roots(a, b, c):
    if a == 0:
        if b == 0:
            return "Invalid: a and b cannot be 0"
        else:
            # Linear equation
            return (-c / b,)

    # Calculate the discriminant
    d = (b**2) - (4 * a * c)

    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
    return (root1, root2)




# Test Cases
##### YOUR CODE HERE #####