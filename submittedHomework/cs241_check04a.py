#***********************************************************************
# Program:
#    checkpoint 04a
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:  Demonstrate composition in Python (a class that
# contains another).
#***********************************************************************
class Person:
    '''information for an author with name and birth year'''
    def __init__(self):
        self.name = "anonymous"
        self.birth_year = "unknown"
    
    def display(self):
        return("{} (b. {})".format(self.name, self.birth_year))



class Book:
    '''information to reference new book entered'''
    def __init__(self):
        self.title = "untitled"
        self.publisher = "unpublished"
        self.author = Person()

    def book_display(self):
        #self.book = Book()
        print("{}\nPublisher:\n{}\nAuthor:\n{}".format(self.title, self.publisher, self.author.display()))

def main():

    book = Book()
    book.book_display()
    print()
    
    print("Please enter the following:")
    book.author.name = input("Name: ")
    book.author.birth_year = int(input("Year: "))
    book.title = input("Title: ")
    book.publisher = input("Publisher: ")
    print()
    book.book_display()
    

if __name__ == "__main__":
    main()  

