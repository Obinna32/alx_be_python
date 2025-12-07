class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book — {self.title} by {self.author}"

class EBook(Book):
    #Represents a digital book with a file size
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    #Represents a printed book with a page count.
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    #Represents a library that stores a collection of book objects
    def __init__(self):
        self.books = []  # Composition: Library *has* books

    def add_book(self, book: Book):
        #Adds a book (Book, EBook, or PrintBook) to the library
        self.books.append(book)

    def list_books(self):
        #Prints details for each book in the library
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook : {book.title} by {book.author}, File Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook : {book.title} by {book.author}, Pages: {book.page_count}")
            else:
                print(f"Book : {book.title} by {book.author}")
