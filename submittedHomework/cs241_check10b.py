#***********************************************************************
# Program:
#    checkpoint 10b
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary: sorting using insertion
#************************************************************************
# testBed cs241/check10b check10b.py
# submit check10b.py

def sort(numbers):
    """
    Fill in this method to sort the list of numbers using insertion,
    this takes in the numbers as a list and using the zeroth as a list 
    takes the number in the next place, 1, and checks to see if it is greater 
    or smaller. greater stays, smaller moves down the list to insert where it fits 
    checking each place along the way.
    """
    for place in range (1, len(numbers)):
        digit = numbers[place]
        value = place
        while value > 0 and numbers[value - 1] > digit:
            numbers[value] = numbers[value - 1]
            value = value - 1
        numbers[value] = digit 

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()
