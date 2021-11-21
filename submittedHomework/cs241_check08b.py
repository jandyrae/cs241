#***********************************************************************
# Program:
#    checkpoint 08b
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary: using encapsulation and properties to solve problems
#************************************************************************
'''Change the variable that you stored the GPA value in to begin with an underscore. 
So, if you previously used self.value it should now be self._value. This signifies to 
others that they should not directly manipulate this variable.

Change your getters and setters to begin with underscores, for example, get_gpa() 

should now be _get_gpa(). Repeat this for set_gpa, get_letter, and set_letter.

Add a property named gpa for the _get_gpa() and _set_gpa(value) functions using the 
syntax: property(_get_gpa, _set_gpa) in your class.

Add a property named letter that calls the _get_letter() and _set_letter(value) 
functions. This time, specify the property using the @property syntax for the getter 
and @letter.setter syntax for the setter. (Please note that when you use the @property 
syntax, you need to change the name of your getter and setter functions to be "letter".)

Change your main function to use these properties instead of calling your functions. In 
other words, all calls to student.get_gpa() should be replaced with student.gpa. All 
calls to student.set_gpa(xx) should be replaced with student.gpa = xx and then the 
same thing for calls to the letter getter and setter.

'''
class GPA:

    def __init__(self):
        self._gpa = 0.0
        

    #@property
    def _get_gpa(self):
        return self._gpa 

    #@gpa.setter    
    def _set_gpa(self, value):
        if value < 0:
            self._gpa = 0.0
        elif value > 4:
            self._gpa = 4.0
        else:
            self._gpa = value

    @property    
    def letter(self):
        if self._gpa <= 0.99:
            return "F"
        elif self._gpa <= 1.99:
            return "D"
        elif self._gpa <= 2.99:
            return "C"
        elif self._gpa <= 3.99:
            return "B"
        else:
            return "A"       


    @letter.setter    
    def letter(self, letter):
        if letter == "F":
            self._gpa = 0.0
        elif letter == "D":
            self._gpa = 1.0
        elif letter == "C":
            self._gpa = 2.0
        elif letter == "B":
            self._gpa = 3.0
        elif letter == "A":
            self._gpa = 4.0      

    gpa = property(_get_gpa, _set_gpa)


                   

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()
