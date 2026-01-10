books = { 'bibek', 'Tamang'}
class Library:
    def __init__(self, books):
        self.available_books = books

    def get_available_books(self):
        return self.available_books
    
    def is_book_available(self, book):
        if self.available_books:
            return True
        else:
            return False