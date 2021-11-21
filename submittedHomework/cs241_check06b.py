#***********************************************************************
# Program:
#    Checkpoint 06b
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:   practice the syntax of inheritance, specifically, the 
# syntax of calling methods from a base class.
#***********************************************************************
class Phone:    
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0
    def prompt_number(self):
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))
    def display(self):
        print(f"Phone info:\n({self.area_code}){self.prefix}-{self.suffix}")

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ""

    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")
    
    def display(self):
        super().display()
        print(f"{self.email}")

def main():
    print("Phone:")
    phone = Phone()
    phone.prompt_number()
    print()
    phone.display()
    print()
    print("Smart phone:")
    smartphone = SmartPhone()
    smartphone.prompt()
    print()
    smartphone.display()

if __name__ == "__main__":
    main()
    

