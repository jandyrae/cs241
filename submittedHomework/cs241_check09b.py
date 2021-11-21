#***********************************************************************
# Program:
#    Checkpoint 09b
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary: exception class
#***************************************
# Write a program that computes the value of 1/n for different 
# values of n. To accomplish this, adhere to the following guidelines:

# Make a function get_inverse that accepts a number, n, and then 
# returns the result 1/n.

# In main, prompt the user for the value, then pass it to your get_inverse, 
# and save the result in a variable. Finally, display the result.

# Create a new exception type: NegativeNumberError that inherits from 
# Exception

# In the get_inverse function you should check for the following rules and 
# raise an appropriate exception. Do not display any error messages in this 
# function, simply raise the exception.

# n is not a number: ValueError
# n is 0: ZeroDivisionError
# n is less than 0: NegativeNumberError
# In main, catch each exception and display the following error messages:
# ValueError: "Error: The value must be a number"
# ZeroDivisionError: "Error: Cannot divide by zero"
# NegativeNumberError: "Error: The value cannot be negative"
# If an exception occurred, do not display the result. If no exception 
# occurred, then display the result as normal.
#testBed cs241/check09b check09b.py
#submit check09b.py



class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)
        

def get_inverse(n):
    # if not n.lstrip("-").isnumeric():
    # try:
        
    # except ValueError: 
        # raise ValueError("Error: The value must be a number") 
    n = int(n)  
    if n < 0:
        raise NegativeNumberError("Error: The value cannot be negative")
    elif n == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero")
#    elif not str(n).isdigit():
 #       raise ValueError("Error: The value must be a number")  
    else:
        return 1.0/n

def main():
    try:
        n = (input("Enter a number: "))
        inverse = get_inverse(n)
        print(f"The result is: {inverse}")
        
    except NegativeNumberError as err:
        print(err)
    except ZeroDivisionError as err:
        print(err)        
    except ValueError as err:
        # print(err)
        print("Error: The value must be a number")

if __name__ == "__main__":
    main()

