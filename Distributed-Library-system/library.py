from Pyro5.api import expose, behavior, serve, Daemon
from user import user
from book import book
from author import author
from datetime import date

@expose
@behavior(instance_mode="single")
class library(object):
    def __init__(self):
        self.authors = []
        self.booksIn = []
        self.booksOut = []
        self.users = []
  
    #task 1
    def add_user(self, user_name):
        user_exists = False
        for person in self.users:
            if user_name == person.user_name:
                print(user_name + " is already in the system.")
                user_exists = True
        if user_exists == False:
            new_user = user(user_name) 
            self.users.append(new_user)
            print(user_name + " has been added.")

    #task 2 
    def return_users(self):
        returning_user_info = []
        for user in self.users:
            returning_user_info.append("Username: " + user.user_name)
        return "\n".join(returning_user_info)

    #task 3
    def add_author(self, author_name, author_genre):
        author_exists= False
        for person in self.authors:
            if author_name == person.author_name:
                print(author_name + " is already in the system.")
                author_exists = True
        if author_exists == False:
            new_author = author(author_name, author_genre)
            self.authors.append(new_author)
            print(author_name + " has been added.")
    
    #task 4
    def return_authors(self):
        returning_author_info = []
        for author in self.authors:
            returning_author_info.append("Author information: " + author.author_name + " writes " + author.author_genre + " books.")
        return "\n".join(returning_author_info)

    #task 5
    def add_book_copy(self, author_name, book_title):
        new_book = book(author_name, book_title)
        self.booksIn.append(new_book)
        print("'" + book_title + "' by: " + author_name + " has been added.")

    #task 6
    def return_books_not_loan(self):
        returning_book_info = []
        for book in self.booksIn:
            returning_book_info.append("'" + book.book_title + "' written by " + book.author_name + " is available to loan.")
        return "\n".join(returning_book_info)

    #task 7
    def loan_book(self, user_name, book_title, year, month, day):
        for book in self.booksIn:
            if book.book_title == book_title:
                #information about loan taking place
                book.loan_year = year
                book.loan_month = month
                book.loan_day = day
                book.loan_user_name = user_name
                #adding book to "out of stock"
                self.booksOut.append(book)
                #returning book back to "in stock" in the library
                self.booksIn.remove(book)
                return 1
            else:
                return 0

    #task 8
    def return_books_loan(self):
        returning_books_loan_info = []
        for book in self.booksOut:
            returning_books_loan_info.append(book.loan_user_name + " loaned: '" + book.book_title + "' on: (" + book.loan_year, book.loan_month, book.loan_day + ")")
        return "\n".join(returning_books_loan_info)

    #task 9
    def return_book(self, user_name, book_title, year, month, day):
        for book in self.booksOut:
            if book.book_title == book_title:
                for user in self.users:
                    if user.user_name == user_name:
                        #adding loan to the users history
                        new_history_item = {}
                        new_history_item["book_title"] = book.book_title
                        new_history_item["start_year"] = book.loan_year
                        new_history_item["start_month"] = book.loan_month
                        new_history_item["start_day"] = book.loan_day
                        new_history_item["end_year"] = year
                        new_history_item["end_month"] = month
                        new_history_item["end_day"] = day
                        user.history.append(new_history_item)
                #returning loan values back to none
                book.loan_year = None
                book.loan_month = None
                book.loan_day = None
                book.loan_user_name = None
                print(book_title + " has been returned to the library.")
                #returning book back to "in stock" in the library
                self.booksIn.append(book)
                #removing from "out on loan"
                self.booksOut.remove(book)

    #task 10
    def delete_book(self, book_title):
        self.booksIn=[x for x in self.booksIn if x.book_title != book_title]
        print(book_title + " has been deleted.")

    #task 11
    def delete_user(self, user_name):
        for user in self.users:
            if user.user_name == user_name:
                books_on_loan = False
                for book in self.booksOut:
                    if book.loan_user_name == user_name:
                        books_on_loan = True
                if len(user.history) == 0 and books_on_loan == False:
                    self.users.remove(user)
                    print(user_name + " has been deleted.")
                else: 
                    print(user_name + " cannot be deleted.")
        
    #task 12
    def user_loans_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day):
        for user in self.users:
            if user.user_name == user_name:
                records_in_range = []
                for record in user.history:
                    start_date = date(start_year, start_month, start_day)
                    end_date = date(end_year, end_month, end_day)
                    #variables for the loan and return dates in the users history
                    my_start = date(record["start_year"],record["start_month"],record["start_day"])
                    my_end = date(record["end_year"],record["end_month"],record["end_day"])
                    if (start_date <= my_start) and (my_end <= end_date ):
                        records_in_range.append("User: " + user_name + "\tloaned: " + str(my_start) + "\treturned: " + str(my_end))
                return "\n".join(records_in_range)


daemon = Daemon() 
serve({library: "example.library"}, daemon=daemon, use_ns=True)
