class Library:
    def __init__(self, books):
        self.available_books = books

    def get_available_books(self):
        return self.available_books
    
    def is_book_available(self, book):
        return book in self.available_books
        # if self.available_books:
        #     return True
        # else:
        #     return False
        
my_book_collection = {'The power of Money', 'Psychology of money', 'The Great gutsby'}

my_library = Library(my_book_collection)

print("My books:",my_library.get_available_books())

print("Is 'The power of Money' available?", my_library.is_book_available('The power of Money'))
print("Is '1920' available?", my_library.is_book_available('1920'))