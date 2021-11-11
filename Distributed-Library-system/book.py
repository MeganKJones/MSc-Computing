
class book(object):
    def __init__(self, author_name, book_title):
        self.author_name = author_name
        self.book_title = book_title
        #values only used if book is out on loan
        self.loan_year = None
        self.loan_month = None
        self.loan_day = None
        self.loan_user_name = None
