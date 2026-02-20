# Brendan Lautissier
# Exercise 1.8 : Loops

# For loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4,...1/10.
"""for i in range(2,11):
    print(1/i)"""

# While loop that asks for a number and prints countdown
# Edgecase of negative numbers
'''n = int(input("Enter a number: "))
if n < 0 :
    print("Sorry, that negative number is negative.")
    print("Be Positive!")
while n >= 0 :
    print(n)
    n -= 1
    if n == 0 :
        print("BOOM!")
        break'''

# Asks for a base number and an exponent number then calculates and prints
'''base = int(input("Enter a base number: "))
exponent = int(input("Enter a exponent number: "))
print(base**exponent)'''

# While loop that asks for a number divisible by 2
# If Number isn't divisible by 2, asks again
'''x = 1
while x % 2 != 0 :
    x = int(input("Enter a number that is divisible by 2: "))
    if x % 2 == 0 :
        print(x, "Congratulations, you are divisible by 2")
    else :
        print(x, "is NOT divisible by 2")
        print("Try again")'''
