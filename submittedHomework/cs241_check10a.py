#***********************************************************************
# Program:
#    checkpoint 10a
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary: sorting using selection
#************************************************************************
# testBed cs241/check10a check10a.py
# submit check10a.py

def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    takes each number and compares it to the others and grabs 
    the highest value and places it at the end, continues until 
    list is in numerical order.
    """
    for each in range(len(numbers)-1, 0, -1):
        highest = 0 
        for every in range(1, each + 1):
            if numbers[every]>numbers[highest]:
                highest = every
        temporary = numbers[each]
        numbers[each] = numbers[highest]
        numbers[highest] = temporary        

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
