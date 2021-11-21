#***********************************************************************
# Program:
#    assignment 03
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:  This assignment will give you practice using classes in
# Python to solve a problem.
#**********************************************************************
class Robot:
    '''Creates a class robot that has x and y movements beginning
    at 10 respectively and is tracking fuel from 100.'''
    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel_amount = 100

    def command(self):
        '''defines the attributes of the class robot and its capabilities'''
        self.move = input("Enter command: ")
        if self.move == "status":
            print("({}, {}) - Fuel: {}".format(self.x, self.y, self.fuel_amount))
            self.command()
        elif self.move == "quit":
            print("Goodbye.")
        elif self.move == "left" and self.fuel_amount >= 5:
            self.x -= 1
            self.fuel_amount -= 5
            self.command()
        elif self.move == "right" and self.fuel_amount >= 5:
            self.x += 1
            self.fuel_amount -= 5
            self.command()
        elif self.move == "up" and self.fuel_amount >= 5:
            self.y -= 1
            self.fuel_amount -= 5
            self.command()
        elif self.move == "down" and self.fuel_amount >= 5:
            self.y += 1
            self.fuel_amount -= 5
            self.command()
        elif self.move == "fire" and self.fuel_amount >= 15:
            self.fuel_amount -= 15
            print("Pew! Pew!")
            self.command()
        elif self.move == "fire" and self.fuel_amount<= 14:
            print("Insufficient fuel to perform action")
            self.command()
        elif self.move == "up" or self.move == "down" or self.move == "left" or self.move == "right" and self.fuel_amount <= 4:
            print("Insufficient fuel to perform action")
            self.command()
        else:
            self.command()
def main():

    robot = Robot() 
    robot.command()

if __name__ == "__main__":
    main()
