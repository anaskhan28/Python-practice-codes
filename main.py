class Library:
    def __init__(self, lsitOfBooks):
        self.books = lsitOfBooks

    def dsiplayAvailableBooks(self):
        print("Books present in Library are: ")
        for books in self.books:
            print(" *" + books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            
            print(f"You have been issued this book {bookName} and we hope you will return it within 30 days!")
            self.books.remove(bookName)
            return True
        else:
            print(" Sorry!! the book has been issued to someone else.. wait till the person return the book")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book.. we hope you enjoyed reading this book.. Have a great day !")


class Student:
    def requestBook(self):
        self.book = input("Enter the book name you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(
        [" Algorithm", " Ikgai", " Till we meet again", " Intelligent Investor"])
    student = Student()
        

        
    # centralLibrary.dsiplayAvailableBooks()
    while(True):
        
        welcomeMsg = '''==== Welcome to Central Library ====
        Please choose an option:
        1.List all the books
        2. Borrow a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.dsiplayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library... Have a great day..!")
            exit()
        else:
            print("Invalid Entry")
