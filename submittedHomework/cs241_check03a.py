#***********************************************************************
# Program:
#    checkpoint 03a
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:  Demonstrate basic classes in Python.
#**********************************************************************
class Student:
    """information for a student including first name, last name, and ID."""

    def __init__(self):
        """holds information for the student"""
        self.first = ""
        self.last = ""
        self.id = 0


def prompt_student():
    user = Student()
    user.first = input("Please enter your first name: ")
    user.last = input("Please enter your last name: ")
    user.id = int(input("Please enter your id number: "))
    return user


def display_student(user):
    print("\nYour information:")
    print("{} - {} {}".format (user.id, user.first, user.last))


def main():
    user = prompt_student()
    display_student(user)

if __name__ == "__main__":
    main()
