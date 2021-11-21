#***********************************************************************
# Program:
#    Checkpoint 06a
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:  work with basic inheritance
#***********************************************************************
class Book:
    '''class for a Book that has the following member variables: title : string author : string publication_year : int'''
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    def display_book_info(self):
        print(f"{self.title} ({self.publication_year}) by {self.author}")

class TextBook(Book):
    '''class for a TextBook that extends a Book and adds the following member variable: subject : string'''
    def __init__(self):
        super().__init__()
        self.subject = ""
        
    def prompt_subject(self):
        self.subject = input("Subject: ") 

    def display_subject(self):
        print(f"Subject: {self.subject}")
    

class PictureBook(Book):
    '''class for a PictureBook that that extends a Book and adds the following member variable: illustrator : string'''
    def __init__(self):
        super().__init__()
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print(f"Illustrated by {self.illustrator}")    

def main():
    book = Book()
    book.prompt_book_info()
    print()
    book.display_book_info()
    print()
    textbook = TextBook()
    textbook.prompt_book_info()
    textbook.prompt_subject()
    print()
    textbook.display_book_info()
    textbook.display_subject()
    print()
    picturebook = PictureBook()
    picturebook.prompt_book_info()
    picturebook.prompt_illustrator()
    print()
    picturebook.display_book_info()
    picturebook.display_illustrator()


if __name__ == "__main__":
    main()

