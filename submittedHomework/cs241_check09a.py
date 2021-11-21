#***********************************************************************
# Program:
#    Checkpoint 09a
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary: exceptions and error
#************************************************************************
#assign04.py
# Write a program that prompts the user for a number and then displays back that number multiplied by 2. 
# Your program should continue to reprompt them as long as they enter a string. To accomplish this, adhere 
# to the following guidelines:

# Your code should assume that the value entered is a valid number and then catch an exception if it's not.

# If an exception is caught, your program should display the text, "The value entered is not valid" and
#  then prompt again.

# It should continue prompting them as long as the value entered is not a number.

# testBed cs241/check09a check09a.py
# submit check09a.py


validInput = False

while not validInput:
    try:
        num = int(input("Enter a number: "))
        validInput = True
    except ValueError:
        print("The value entered is not valid")
result = (2 * num)
print("The result is:", result)

