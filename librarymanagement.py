#library managment system

class Library:
     def __init__(self,listofbooks):
         self.listofbooks = listofbooks
     def books_availabel(self):

         print("Books available")
         print()
         for books in self.listofbooks:
            print(books)


     def lend_books(self):
         if requestedbook in self.listofbooks:
             print("You have borrowed the books: ")
             self.listofbooks.remove(requestedbook)
         else:
             print("The book is not available in list")





     def add_books(self):
        pass


class customer():
    def requestedbook(self):
        self.books = input("Enter the name of the book: ")
        return self.books



library = Library(["the god of war" , "the journey" , "around the world" , "last of us"])
library.books_availabel()
library.lend_books()
Customer = customer()
Customer.requestedbook()
