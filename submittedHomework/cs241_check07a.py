#***********************************************************************
# Program:
#    Checkpoint 07a
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:  work with abstract and polymorphism
#***********************************************************************
#testBed cs241/check07a check07a.py
#submit check07a.py
class Car:
    def __init__(self, name):
        self.name = "Unknown model"
        
    def get_door_specs(self):
        return "Unknown doors"


class Civic(Car):
    def __init__(self):
        self.name = "Civic"        
    
    def get_door_specs(self):
        return "4 doors"


class Odyssey(Car):
    def __init__(self):
        self.name = "Odyssey"
    
    def get_door_specs(self):
        return "2 front doors, 2 sliding doors, 1 tail gate"


class Ferrari(Car):
    def __init__(self):
        self.name = "Ferrari"
    
    def get_door_specs(self):
        return "2 butterfly doors"


def attach_doors(car):
        print(f"Attaching doors to {car.name} - {car.get_door_specs()}")

def main():
    car1 = Civic()
    car2 = Odyssey()
    car3 = Ferrari()

    attach_doors(car1)
    attach_doors(car2)
    attach_doors(car3)

if __name__ == "__main__":
    main()
    

